import re
from textwrap import shorten
from ..config import settings
from .openai_client import get_openai_client

def _split_sentences(text: str) -> list[str]:
    return [p.strip() for p in re.split(r'(?<=[.!?])\s+', text.strip()) if p.strip()]

def _to_bullets(sentences: list[str], max_items: int = 5) -> str:
    return "\n".join(
        f"- {shorten(s, width=180, placeholder='…')}" for s in sentences[:max_items]
    ) or "- (no content)"

def _heuristic_summarize(text: str, style: str) -> str:
    sents = _split_sentences(text)
    if not sents:
        return "(empty input)"
    if style == "bullets":
        return _to_bullets(sents, max_items=7)
    if style == "detailed":
        return " ".join(sents[:5] if len(sents) > 5 else sents)
    return " ".join(sents[:3])  # concise

def summarize(text: str, style: str = "concise") -> str:
    client = get_openai_client()
    if not client:
        return _heuristic_summarize(text, style)

    # Prompt templates
    style_prompts = {
        "concise": "Summarize the text in 2–3 crisp sentences.",
        "detailed": "Write a detailed multi-sentence summary that captures key points.",
        "bullets": "Summarize into clear bullet points (3–7 items).",
    }
    instruction = style_prompts.get(style, style_prompts["concise"])
    user_prompt = f"{instruction}\n\n---\n{text}\n---"

    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Summarization assistant."},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=400,
            temperature=0.3,
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return _heuristic_summarize(text, style) + f"\n\n[Note: OpenAI error: {e}]"
