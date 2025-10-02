import re
from textwrap import shorten

def _split_sentences(text: str) -> list[str]:
    # simple sentence split; fast and “good enough” for stub
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return [p.strip() for p in parts if p.strip()]

def _to_bullets(sentences: list[str], max_items: int = 5) -> str:
    bullets = [f"- {shorten(s, width=180, placeholder='…')}" for s in sentences[:max_items]]
    return "\n".join(bullets) if bullets else "- (no content)"

def summarize(text: str, style: str = "concise") -> str:
    sentences = _split_sentences(text)

    if not sentences:
        return "(empty input)"

    if style == "bullets":
        return _to_bullets(sentences, max_items=7)
    if style == "detailed":
        # keep the first ~5 sentences (fallback to full if short)
        chosen = sentences[:5] if len(sentences) > 5 else sentences
        return " ".join(chosen)
    # concise (default): 1–3 sentences
    chosen = sentences[:3] if len(sentences) > 2 else sentences
    return " ".join(chosen)
