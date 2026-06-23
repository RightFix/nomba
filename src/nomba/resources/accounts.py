# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
from __future__ import annotations

from .. import models as _models
from ..http import AsyncNombaClient, NombaClient
from ..validation import validate_body


class Accounts:
    """Sync resource methods for the Accounts group."""

    def __init__(self, client: NombaClient) -> None:
        self._client = client

    def list_all_accounts(self, *, limit: str | None = None, cursor: str | None = None, **extra: object) -> _models.ListAllAccountsResponse:
        """
        List all sub accounts

        You can use this endpoints to fetch all the accounts tied to a business. Accounts are sorted by date, with the most recently-created account appearing first.
        """
        path = "/v1/accounts"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def create_a_sub_account(self, account_ref, phone_number, email, bvn, pin, account_name, currency, *, callback_url: object | None = None, expiry_date: object | None = None, **extra: object) -> _models.CreateASubAccountResponse:
        """
        Create a sub account

        You can use this endpoint to create a sub account that is part of your business.

        Body fields:
            accountRef (required): Account reference
            phoneNumber (required): Phone number
            email (required): Email address
            bvn (required): Bank Verification Number (BVN)
            pin (required): Personal Identification Number (PIN)
            accountName (required): Account holder's name
            currency (required): Currency code
            callbackUrl: Callback url
            expiryDate: Expiry date
        """
        path = "/v1/accounts"
        params = None
        body: dict[str, object] = {}
        body["accountRef"] = account_ref
        body["phoneNumber"] = phone_number
        body["email"] = email
        body["bvn"] = bvn
        body["pin"] = pin
        body["accountName"] = account_name
        body["currency"] = currency
        if callback_url is not None:
            body["callbackUrl"] = callback_url
        if expiry_date is not None:
            body["expiryDate"] = expiry_date
        body.update(extra)
        validate_body("post", "/v1/accounts", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def fetch_account_details(self, *, account_id: str | None = None, account_ref: str | None = None, **extra: object) -> _models.FetchAccountDetailsResponse:
        """
        Fetch details of a sub account

        You can use this endpoint to get details of a sub account.
        """
        path = "/v1/accounts/sub-account-details"
        params: dict[str, object] = {}
        if account_id is not None:
            params["accountId"] = account_id
        if account_ref is not None:
            params["accountRef"] = account_ref
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def fetch_parent_account_details(self, **extra: object) -> _models.FetchParentAccountDetailsResponse:
        """
        Fetch parent account details

        You can use this endpoint to get details of the parent account.
        """
        path = "/v1/accounts/parent"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def fetch_account_balance(self, sub_account_id: str, **extra: object) -> _models.FetchAccountBalanceResponse:
        """
        Fetch sub account balance

        You can use this endpoint to get the balance of a sub account
        """
        path = f"/v1/accounts/{sub_account_id}/balance"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def fetch_parent_account_balance(self, **extra: object) -> _models.FetchParentAccountBalanceResponse:
        """
        Fetch parent account balance

        You can use this endpoint to get the balance of the parent account.
        """
        path = "/v1/accounts/balance"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def suspend_an_account(self, sub_account_id: str, **extra: object) -> _models.SuspendAnAccountResponse:
        """
        Suspend a sub account

        You can use this endpoint to suspend a sub account.
        """
        path = f"/v1/accounts/suspend/{sub_account_id}"
        params = None
        return self._client.put(path, params=params)  # type: ignore[return-value]

    def reactivate_a_sub_account(self, sub_account_id: str, **extra: object) -> _models.ReactivateASubAccountResponse:
        """
        Reactivate a sub account

        You can use this endpoint to reactivate a sub account
        """
        path = f"/v1/accounts/reactivate/{sub_account_id}"
        params = None
        return self._client.put(path, params=params)  # type: ignore[return-value]

    def fetch_terminals_assigned_to_an_account(self, sub_account_id: str, *, limit: str | None = None, cursor: str | None = None, terminal_id: str | None = None, serial_number: str | None = None, terminal_label: str | None = None, merchant_name: str | None = None, **extra: object) -> _models.FetchTerminalsAssignedToAnAccountResponse:
        """
        Fetch terminals assigned to a sub account

        You can use this endpoint to fetch terminals linked to a sub account
        """
        path = f"/v1/accounts/{sub_account_id}/terminals"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if terminal_id is not None:
            params["terminalId"] = terminal_id
        if serial_number is not None:
            params["serialNumber"] = serial_number
        if terminal_label is not None:
            params["terminalLabel"] = terminal_label
        if merchant_name is not None:
            params["merchantName"] = merchant_name
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def fetch_terminals_assigned_to_the_parent_account(self, *, limit: str | None = None, cursor: str | None = None, terminal_id: str | None = None, serial_number: str | None = None, terminal_label: str | None = None, merchant_name: str | None = None, **extra: object) -> _models.FetchTerminalsAssignedToTheParentAccountResponse:
        """
        Fetch terminals assigned to the parent account

        You can use this endpoint to fetch terminals linked to the parent account.
        """
        path = "/v1/accounts/terminals"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if terminal_id is not None:
            params["terminalId"] = terminal_id
        if serial_number is not None:
            params["serialNumber"] = serial_number
        if terminal_label is not None:
            params["terminalLabel"] = terminal_label
        if merchant_name is not None:
            params["merchantName"] = merchant_name
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def update_access_to_account(self, sub_account_id: str, grant_type, client_id, role, **extra: object) -> _models.UpdateAccessToAccountResponse:
        """
        Update access to account

        You can use this endpoint to update the access of an api client within an account.

        Body fields:
            grantType (required): The action to perform on the access
            clientId (required): The client to grant/deny access to the account
            role (required): The role to assume within the account
        """
        path = f"/v1/accounts/{sub_account_id}/access"
        params = None
        body: dict[str, object] = {}
        body["grantType"] = grant_type
        body["clientId"] = client_id
        body["role"] = role
        body.update(extra)
        validate_body("put", "/v1/accounts/{subAccountId}/access", body)
        return self._client.put(path, json=body, params=params)  # type: ignore[return-value]



class AsyncAccounts:
    """Async resource methods for the Accounts group."""

    def __init__(self, client: AsyncNombaClient) -> None:
        self._client = client

    async def list_all_accounts(self, *, limit: str | None = None, cursor: str | None = None, **extra: object) -> _models.ListAllAccountsResponse:
        """
        List all sub accounts

        You can use this endpoints to fetch all the accounts tied to a business. Accounts are sorted by date, with the most recently-created account appearing first.
        """
        path = "/v1/accounts"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def create_a_sub_account(self, account_ref, phone_number, email, bvn, pin, account_name, currency, *, callback_url: object | None = None, expiry_date: object | None = None, **extra: object) -> _models.CreateASubAccountResponse:
        """
        Create a sub account

        You can use this endpoint to create a sub account that is part of your business.

        Body fields:
            accountRef (required): Account reference
            phoneNumber (required): Phone number
            email (required): Email address
            bvn (required): Bank Verification Number (BVN)
            pin (required): Personal Identification Number (PIN)
            accountName (required): Account holder's name
            currency (required): Currency code
            callbackUrl: Callback url
            expiryDate: Expiry date
        """
        path = "/v1/accounts"
        params = None
        body: dict[str, object] = {}
        body["accountRef"] = account_ref
        body["phoneNumber"] = phone_number
        body["email"] = email
        body["bvn"] = bvn
        body["pin"] = pin
        body["accountName"] = account_name
        body["currency"] = currency
        if callback_url is not None:
            body["callbackUrl"] = callback_url
        if expiry_date is not None:
            body["expiryDate"] = expiry_date
        body.update(extra)
        validate_body("post", "/v1/accounts", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def fetch_account_details(self, *, account_id: str | None = None, account_ref: str | None = None, **extra: object) -> _models.FetchAccountDetailsResponse:
        """
        Fetch details of a sub account

        You can use this endpoint to get details of a sub account.
        """
        path = "/v1/accounts/sub-account-details"
        params: dict[str, object] = {}
        if account_id is not None:
            params["accountId"] = account_id
        if account_ref is not None:
            params["accountRef"] = account_ref
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def fetch_parent_account_details(self, **extra: object) -> _models.FetchParentAccountDetailsResponse:
        """
        Fetch parent account details

        You can use this endpoint to get details of the parent account.
        """
        path = "/v1/accounts/parent"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def fetch_account_balance(self, sub_account_id: str, **extra: object) -> _models.FetchAccountBalanceResponse:
        """
        Fetch sub account balance

        You can use this endpoint to get the balance of a sub account
        """
        path = f"/v1/accounts/{sub_account_id}/balance"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def fetch_parent_account_balance(self, **extra: object) -> _models.FetchParentAccountBalanceResponse:
        """
        Fetch parent account balance

        You can use this endpoint to get the balance of the parent account.
        """
        path = "/v1/accounts/balance"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def suspend_an_account(self, sub_account_id: str, **extra: object) -> _models.SuspendAnAccountResponse:
        """
        Suspend a sub account

        You can use this endpoint to suspend a sub account.
        """
        path = f"/v1/accounts/suspend/{sub_account_id}"
        params = None
        return await self._client.put(path, params=params)  # type: ignore[return-value]

    async def reactivate_a_sub_account(self, sub_account_id: str, **extra: object) -> _models.ReactivateASubAccountResponse:
        """
        Reactivate a sub account

        You can use this endpoint to reactivate a sub account
        """
        path = f"/v1/accounts/reactivate/{sub_account_id}"
        params = None
        return await self._client.put(path, params=params)  # type: ignore[return-value]

    async def fetch_terminals_assigned_to_an_account(self, sub_account_id: str, *, limit: str | None = None, cursor: str | None = None, terminal_id: str | None = None, serial_number: str | None = None, terminal_label: str | None = None, merchant_name: str | None = None, **extra: object) -> _models.FetchTerminalsAssignedToAnAccountResponse:
        """
        Fetch terminals assigned to a sub account

        You can use this endpoint to fetch terminals linked to a sub account
        """
        path = f"/v1/accounts/{sub_account_id}/terminals"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if terminal_id is not None:
            params["terminalId"] = terminal_id
        if serial_number is not None:
            params["serialNumber"] = serial_number
        if terminal_label is not None:
            params["terminalLabel"] = terminal_label
        if merchant_name is not None:
            params["merchantName"] = merchant_name
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def fetch_terminals_assigned_to_the_parent_account(self, *, limit: str | None = None, cursor: str | None = None, terminal_id: str | None = None, serial_number: str | None = None, terminal_label: str | None = None, merchant_name: str | None = None, **extra: object) -> _models.FetchTerminalsAssignedToTheParentAccountResponse:
        """
        Fetch terminals assigned to the parent account

        You can use this endpoint to fetch terminals linked to the parent account.
        """
        path = "/v1/accounts/terminals"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if terminal_id is not None:
            params["terminalId"] = terminal_id
        if serial_number is not None:
            params["serialNumber"] = serial_number
        if terminal_label is not None:
            params["terminalLabel"] = terminal_label
        if merchant_name is not None:
            params["merchantName"] = merchant_name
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def update_access_to_account(self, sub_account_id: str, grant_type, client_id, role, **extra: object) -> _models.UpdateAccessToAccountResponse:
        """
        Update access to account

        You can use this endpoint to update the access of an api client within an account.

        Body fields:
            grantType (required): The action to perform on the access
            clientId (required): The client to grant/deny access to the account
            role (required): The role to assume within the account
        """
        path = f"/v1/accounts/{sub_account_id}/access"
        params = None
        body: dict[str, object] = {}
        body["grantType"] = grant_type
        body["clientId"] = client_id
        body["role"] = role
        body.update(extra)
        validate_body("put", "/v1/accounts/{subAccountId}/access", body)
        return await self._client.put(path, json=body, params=params)  # type: ignore[return-value]

