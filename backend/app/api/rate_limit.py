import time
from fastapi import Request, HTTPException

_request_counts: dict[str, tuple[int, float]] = {}

MAX_REQUESTS = 3
WINDOW = 60.0

def check_rate_limit(request: Request):
    ip = request.client.host if request.client else "unknown"
    now = time.time()

    count, reset_at = _request_counts.get(ip, (0, now + WINDOW))

    if now > reset_at:

        count = 0
        reset_at = now + WINDOW

    if count >= MAX_REQUESTS:
        retry_after = int(reset_at - now)
        raise HTTPException(
            status_code=429,
            detail=f"Rate limit exceeded. Try again in {retry_after}s.",
            headers={"Retry-After": str(retry_after)},
        )

    _request_counts[ip] = (count + 1, reset_at)
