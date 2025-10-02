import re
from textwrap import shorten
from ..config import settings
from .openai_client import get_openai_client


def _split_sentences(text: str) -> list[str]:
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return [p.strip() for p in parts if p.strip()]


def _to_bullets(sentences: list[str], max_items: int = 5) -> str:
    bullets = [f"- {shorten(s, width=180, placeholder='…')}" for s in sentences[:max_items]]
    return "\n".join(bullets) if bullets else "- (no content)"


def _heuristic_summarize(text: str, style: str) -> str:
    sentences = _split_sentences(text)
    if not sentences:
        return "(empty input)"
    if style == "bullets":
        return _to_bullets(sentences, max_items=7)
    if style == "detailed":
        chosen = sentences[:5] if len(sentences) > 5 else sentences
        return " ".join(chosen)
    chosen = sentences[:3] if len(sentences) > 2 else sentences
    return " ".join(chosen)


def summarize(text: str, style: str = "concise") -> str:
    client = get_openai_client()
    if not client:
        return _heuristic_summarize(text, style)

    prompt = (
        f"Summarize the following text in a {style} style.\n\n"
        f"---\n{text}\n---"
    )

    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful summarization assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=300,
            temperature=0.3,
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        # Fallback gracefully
        return _heuristic_summarize(text, style) + f"\n\n[Note: OpenAI error: {e}]"
