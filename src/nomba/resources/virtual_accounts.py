# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
from __future__ import annotations


from ..http import AsyncNombaClient, NombaClient
from ..validation import validate_body
from .. import models as _models


class VirtualAccounts:
    """Sync resource methods for the VirtualAccounts group."""

    def __init__(self, client: NombaClient) -> None:
        self._client = client

    def create_virtual_account(self, account_ref, account_name, **extra: object) -> _models.CreateVirtualAccountResponse:
        """
        Create virtual account

        You can use this endpoint to create a virtual account to receive payments.

        Body fields:
            accountRef (required): Account reference
            accountName (required): Account holder's name
        """
        path = "/v1/accounts/virtual"
        params = None
        body: dict[str, object] = {}
        body["accountRef"] = account_ref
        body["accountName"] = account_name
        body.update(extra)
        validate_body("post", "/v1/accounts/virtual", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def filter_virtual_accounts(self, *, limit: str | None = None, cursor: str | None = None, account_name: object | None = None, account_ref: object | None = None, bvn: object | None = None, bank_account_number: object | None = None, date_created_from: object | None = None, date_created_to: object | None = None, expired: object | None = None, resource_acquired: object | None = None, **extra: object) -> _models.FilterVirtualAccountsResponse:
        """
        Filter virtual accounts

        You can use this endpoint to filter your virtual accounts.

        Body fields:
            accountName: Account holder's name
            accountRef: Account reference
            bvn: Bank Verification Number (BVN)
            bankAccountNumber: Bank account number
            dateCreatedFrom: Date created from
            dateCreatedTo: Date created to
            expired: Whether the virtual account is expired or not
            resourceAcquired: Whether the virtual account is in use or not
        """
        path = "/v1/accounts/virtual/list"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        body: dict[str, object] = {}
        if account_name is not None:
            body["accountName"] = account_name
        if account_ref is not None:
            body["accountRef"] = account_ref
        if bvn is not None:
            body["bvn"] = bvn
        if bank_account_number is not None:
            body["bankAccountNumber"] = bank_account_number
        if date_created_from is not None:
            body["dateCreatedFrom"] = date_created_from
        if date_created_to is not None:
            body["dateCreatedTo"] = date_created_to
        if expired is not None:
            body["expired"] = expired
        if resource_acquired is not None:
            body["resourceAcquired"] = resource_acquired
        body.update(extra)
        validate_body("post", "/v1/accounts/virtual/list", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def update_a_virtual_account(self, account_ref: str, *, account_name: object | None = None, callback_url: object | None = None, **extra: object) -> _models.UpdateAVirtualAccountResponse:
        """
        Update a virtual account

        You can use this endpoint to update a virtual account.

        Body fields:
            accountName: Account holder's name
            callbackUrl: Callback url
        """
        path = f"/v1/accounts/virtual/{account_ref}"
        params = None
        body: dict[str, object] = {}
        if account_name is not None:
            body["accountName"] = account_name
        if callback_url is not None:
            body["callbackUrl"] = callback_url
        body.update(extra)
        validate_body("put", "/v1/accounts/virtual/{accountRef}", body)
        return self._client.put(path, json=body, params=params)  # type: ignore[return-value]

    def fetch_a_virtual_account(self, account_ref: str, **extra: object) -> _models.FetchAVirtualAccountResponse:
        """
        Fetch a virtual account

        You can use this endpoint to fetch a virtual account.
        """
        path = f"/v1/accounts/virtual/{account_ref}"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def expire_a_virtual_account(self, account_ref: str, **extra: object) -> _models.ExpireAVirtualAccountResponse:
        """
        Expire a virtual account

        You can use this endpoint to expire a virtual account.
        """
        path = f"/v1/accounts/virtual/{account_ref}"
        params = None
        return self._client.delete(path, params=params)  # type: ignore[return-value]



class AsyncVirtualAccounts:
    """Async resource methods for the VirtualAccounts group."""

    def __init__(self, client: AsyncNombaClient) -> None:
        self._client = client

    async def create_virtual_account(self, account_ref, account_name, **extra: object) -> _models.CreateVirtualAccountResponse:
        """
        Create virtual account

        You can use this endpoint to create a virtual account to receive payments.

        Body fields:
            accountRef (required): Account reference
            accountName (required): Account holder's name
        """
        path = "/v1/accounts/virtual"
        params = None
        body: dict[str, object] = {}
        body["accountRef"] = account_ref
        body["accountName"] = account_name
        body.update(extra)
        validate_body("post", "/v1/accounts/virtual", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def filter_virtual_accounts(self, *, limit: str | None = None, cursor: str | None = None, account_name: object | None = None, account_ref: object | None = None, bvn: object | None = None, bank_account_number: object | None = None, date_created_from: object | None = None, date_created_to: object | None = None, expired: object | None = None, resource_acquired: object | None = None, **extra: object) -> _models.FilterVirtualAccountsResponse:
        """
        Filter virtual accounts

        You can use this endpoint to filter your virtual accounts.

        Body fields:
            accountName: Account holder's name
            accountRef: Account reference
            bvn: Bank Verification Number (BVN)
            bankAccountNumber: Bank account number
            dateCreatedFrom: Date created from
            dateCreatedTo: Date created to
            expired: Whether the virtual account is expired or not
            resourceAcquired: Whether the virtual account is in use or not
        """
        path = "/v1/accounts/virtual/list"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        body: dict[str, object] = {}
        if account_name is not None:
            body["accountName"] = account_name
        if account_ref is not None:
            body["accountRef"] = account_ref
        if bvn is not None:
            body["bvn"] = bvn
        if bank_account_number is not None:
            body["bankAccountNumber"] = bank_account_number
        if date_created_from is not None:
            body["dateCreatedFrom"] = date_created_from
        if date_created_to is not None:
            body["dateCreatedTo"] = date_created_to
        if expired is not None:
            body["expired"] = expired
        if resource_acquired is not None:
            body["resourceAcquired"] = resource_acquired
        body.update(extra)
        validate_body("post", "/v1/accounts/virtual/list", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def update_a_virtual_account(self, account_ref: str, *, account_name: object | None = None, callback_url: object | None = None, **extra: object) -> _models.UpdateAVirtualAccountResponse:
        """
        Update a virtual account

        You can use this endpoint to update a virtual account.

        Body fields:
            accountName: Account holder's name
            callbackUrl: Callback url
        """
        path = f"/v1/accounts/virtual/{account_ref}"
        params = None
        body: dict[str, object] = {}
        if account_name is not None:
            body["accountName"] = account_name
        if callback_url is not None:
            body["callbackUrl"] = callback_url
        body.update(extra)
        validate_body("put", "/v1/accounts/virtual/{accountRef}", body)
        return await self._client.put(path, json=body, params=params)  # type: ignore[return-value]

    async def fetch_a_virtual_account(self, account_ref: str, **extra: object) -> _models.FetchAVirtualAccountResponse:
        """
        Fetch a virtual account

        You can use this endpoint to fetch a virtual account.
        """
        path = f"/v1/accounts/virtual/{account_ref}"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def expire_a_virtual_account(self, account_ref: str, **extra: object) -> _models.ExpireAVirtualAccountResponse:
        """
        Expire a virtual account

        You can use this endpoint to expire a virtual account.
        """
        path = f"/v1/accounts/virtual/{account_ref}"
        params = None
        return await self._client.delete(path, params=params)  # type: ignore[return-value]

