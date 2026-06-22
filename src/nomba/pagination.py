"""
Generic cursor-pagination helpers.

Nomba's own API is cursor-paginated for list-style endpoints (it returns a
`cursor` field you feed back in as the `cursor` query/body param for the next
page). These helpers just drive that loop for you — they do not introduce a
second, separate pagination scheme.

Endpoints confirmed paginated by Nomba (per their OpenAPI spec — each returns
`results` + `cursor`, either at the top level or nested under `data`):
    - accounts.list_all_accounts
    - accounts.fetch_terminals_assigned_to_an_account
    - accounts.fetch_terminals_assigned_to_the_parent_account
    - virtual_accounts.filter_virtual_accounts
    - transactions.fetch_credit_debit_transactions_on_a_sub_account
    - transactions.fetch_credit_debit_transactions_on_the_parent_account
    - transactions.fetch_transactions_on_a_sub_account
    - transactions.filter_account_transactions
    - transactions.fetch_transactions_on_the_parent_account
    - transactions.filter_parent_account_transactions
"""
from __future__ import annotations

from typing import Any, AsyncIterator, Callable, Iterator


def _unwrap(response: dict[str, Any]) -> dict[str, Any]:
    """Nomba wraps some list responses in {code, description, data: {...}}
    and returns others unwrapped as {results, cursor} directly."""
    if "results" in response or "cursor" in response:
        return response
    data = response.get("data")
    if isinstance(data, dict):
        return data
    return response


def paginate(
    method: Callable[..., dict[str, Any]],
    *,
    limit: int | None = None,
    **kwargs: Any,
) -> Iterator[dict[str, Any]]:
    """
    Iterate over every item across all pages of a paginated Nomba endpoint.

    Example:
        from nomba import Nomba
        from nomba.pagination import paginate

        nomba = Nomba(...)
        for account in paginate(nomba.accounts.list_all_accounts, limit=50):
            print(account["accountRef"])

    Works with any bound resource method that accepts a `cursor` kwarg and
    returns a `results` list + `cursor` string (see module docstring for the
    confirmed list of such endpoints).
    """
    cursor: str | None = None
    while True:
        call_kwargs = dict(kwargs)
        if limit is not None:
            call_kwargs["limit"] = limit
        if cursor is not None:
            call_kwargs["cursor"] = cursor

        response = method(**call_kwargs)
        page = _unwrap(response)
        results = page.get("results") or []
        for item in results:
            yield item

        cursor = page.get("cursor") or None
        if not cursor or not results:
            break


async def apaginate(
    method: Callable[..., Any],
    *,
    limit: int | None = None,
    **kwargs: Any,
) -> AsyncIterator[dict[str, Any]]:
    """
    Async version of `paginate`. `method` must be an async resource method.

    Example:
        from nomba import AsyncNomba
        from nomba.pagination import apaginate

        async with AsyncNomba(...) as nomba:
            async for account in apaginate(nomba.accounts.list_all_accounts, limit=50):
                print(account["accountRef"])
    """
    cursor: str | None = None
    while True:
        call_kwargs = dict(kwargs)
        if limit is not None:
            call_kwargs["limit"] = limit
        if cursor is not None:
            call_kwargs["cursor"] = cursor

        response = await method(**call_kwargs)
        page = _unwrap(response)
        results = page.get("results") or []
        for item in results:
            yield item

        cursor = page.get("cursor") or None
        if not cursor or not results:
            break
