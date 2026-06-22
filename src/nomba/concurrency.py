"""
Bounded concurrency helper.

`asyncio.gather` has no built-in concurrency limit -- firing off 200 async
calls with `asyncio.gather(*[nomba.transfers.send(...) for ...])` sends all
200 at once. If several start failing (e.g. Nomba rate-limiting you), each
one independently retries with its own backoff, multiplying load right when
the API is already struggling, and you may also just trip the rate limit by
bursting too many requests in the same window.

`gather_limited` runs the same calls but caps how many are in flight at
once, which keeps both the retry storm and the burst size bounded.
"""
from __future__ import annotations

import asyncio
from typing import Awaitable, Callable, Sequence, TypeVar

T = TypeVar("T")


async def gather_limited(
    calls: Sequence[Callable[[], Awaitable[T]]],
    *,
    limit: int = 5,
    return_exceptions: bool = False,
) -> list[T| BaseException]:
    """
    Run a sequence of zero-arg async callables with at most `limit` running
    concurrently, preserving input order in the returned results.

    Example:
        from nomba import AsyncNomba
        from nomba.concurrency import gather_limited

        async with AsyncNomba(...) as nomba:
            calls = [
                (lambda ref=ref: nomba.virtual_accounts.fetch_a_virtual_account(ref))
                for ref in account_refs
            ]
            results = await gather_limited(calls, limit=5)

    `return_exceptions=True` behaves like `asyncio.gather(..., return_exceptions=True)`:
    exceptions are returned in place of results instead of propagating.
    """
    semaphore = asyncio.Semaphore(limit)

    async def _run(call: Callable[[], Awaitable[T]]) -> T:
        async with semaphore:
            return await call()

    return await asyncio.gather(
        *(_run(call) for call in calls), return_exceptions=return_exceptions
    )
