# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
from __future__ import annotations


from ..http import AsyncNombaClient, NombaClient
from ..validation import validate_body
from .. import models as _models


class Transfers:
    """Sync resource methods for the Transfers group."""

    def __init__(self, client: NombaClient) -> None:
        self._client = client

    def fetch_bank_codes_and_names(self, **extra: object) -> _models.FetchBankCodesAndNamesResponse:
        """
        Fetch bank codes and names

        You can use this endpoint to fetch all banks, their names and codes.
        """
        path = "/v1/transfers/banks"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def perform_bank_account_lookup(self, account_number, bank_code, **extra: object) -> _models.PerformBankAccountLookupResponse:
        """
        Perform bank account lookup

        You can use this endpoint to perform bank account lookup.

        Body fields:
            accountNumber (required): The account number to be looked up.
            bankCode (required): The bankCode of the bank the account number belongs to. This can be obtained from a call to `/v1/transfers/bank` 
        """
        path = "/v1/transfers/bank/lookup"
        params = None
        body: dict[str, object] = {}
        body["accountNumber"] = account_number
        body["bankCode"] = bank_code
        body.update(extra)
        validate_body("post", "/v1/transfers/bank/lookup", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def perform_bank_account_transfer_the_parent_account(self, amount, account_number, account_name, bank_code, merchant_tx_ref, sender_name, *, narration: object | None = None, **extra: object) -> _models.PerformBankAccountTransferTheParentAccountResponse:
        """
        Perform bank account transfer from the parent account

        You can use this endpoint to perform bank account transfer.

        Body fields:
            amount (required): The amount to be transferred.
            accountNumber (required): The destination bank account number.
            accountName (required): The name on the account.
            bankCode (required): The code of the recipient bank.
            merchantTxRef (required): Unique reference used to track a transaction from an external process.
            senderName (required): Sender name
            narration: The payment narration
        """
        path = "/v1/transfers/bank"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["accountNumber"] = account_number
        body["accountName"] = account_name
        body["bankCode"] = bank_code
        body["merchantTxRef"] = merchant_tx_ref
        body["senderName"] = sender_name
        if narration is not None:
            body["narration"] = narration
        body.update(extra)
        validate_body("post", "/v1/transfers/bank", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def perform_bank_account_transfer_from_account(self, sub_account_id: str, amount, account_number, account_name, bank_code, merchant_tx_ref, sender_name, *, narration: object | None = None, **extra: object) -> _models.PerformBankAccountTransferFromAccountResponse:
        """
        Perform bank account transfer from a sub account

        You can use this endpoint to perform bank account transfer using a sub account

        Body fields:
            amount (required): The amount to be transferred.
            accountNumber (required): The destination bank account number.
            accountName (required): The name on the account.
            bankCode (required): The code of the recipient bank.
            merchantTxRef (required): Unique reference used to track a transaction from an external process.
            senderName (required): Sender name
            narration: The payment narration
        """
        path = f"/v1/transfers/bank/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["accountNumber"] = account_number
        body["accountName"] = account_name
        body["bankCode"] = bank_code
        body["merchantTxRef"] = merchant_tx_ref
        body["senderName"] = sender_name
        if narration is not None:
            body["narration"] = narration
        body.update(extra)
        validate_body("post", "/v1/transfers/bank/{subAccountId}", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def perform_wallet_transfer_from_the_parent_account(self, amount, receiver_account_id, merchant_tx_ref, *, narration: object | None = None, **extra: object) -> _models.PerformWalletTransferFromTheParentAccountResponse:
        """
        Perform wallet transfer from the parent account

        You can use this endpoint to perform a wallet transfer.

        Body fields:
            amount (required): The amount to be transferred.
            receiverAccountId (required): The receiver's accountId.
            merchantTxRef (required): Unique reference used to track a transaction from an external process.
            narration: The payment narration
        """
        path = "/v1/transfers/wallet"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["receiverAccountId"] = receiver_account_id
        body["merchantTxRef"] = merchant_tx_ref
        if narration is not None:
            body["narration"] = narration
        body.update(extra)
        validate_body("post", "/v1/transfers/wallet", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def perform_wallet_transfer_from_a_sub_account(self, sub_account_id: str, amount, receiver_account_id, merchant_tx_ref, *, narration: object | None = None, **extra: object) -> _models.PerformWalletTransferFromASubAccountResponse:
        """
        Perform wallet transfer from a sub account

        You can use this endpoint to perform a wallet transfer from a sub account

        Body fields:
            amount (required): The amount to be transferred.
            receiverAccountId (required): The receiver's accountId.
            merchantTxRef (required): Unique reference used to track a transaction from an external process.
            narration: The payment narration
        """
        path = f"/v1/transfers/wallet/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["receiverAccountId"] = receiver_account_id
        body["merchantTxRef"] = merchant_tx_ref
        if narration is not None:
            body["narration"] = narration
        body.update(extra)
        validate_body("post", "/v1/transfers/wallet/{subAccountId}", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]



class AsyncTransfers:
    """Async resource methods for the Transfers group."""

    def __init__(self, client: AsyncNombaClient) -> None:
        self._client = client

    async def fetch_bank_codes_and_names(self, **extra: object) -> _models.FetchBankCodesAndNamesResponse:
        """
        Fetch bank codes and names

        You can use this endpoint to fetch all banks, their names and codes.
        """
        path = "/v1/transfers/banks"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def perform_bank_account_lookup(self, account_number, bank_code, **extra: object) -> _models.PerformBankAccountLookupResponse:
        """
        Perform bank account lookup

        You can use this endpoint to perform bank account lookup.

        Body fields:
            accountNumber (required): The account number to be looked up.
            bankCode (required): The bankCode of the bank the account number belongs to. This can be obtained from a call to `/v1/transfers/bank` 
        """
        path = "/v1/transfers/bank/lookup"
        params = None
        body: dict[str, object] = {}
        body["accountNumber"] = account_number
        body["bankCode"] = bank_code
        body.update(extra)
        validate_body("post", "/v1/transfers/bank/lookup", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def perform_bank_account_transfer_the_parent_account(self, amount, account_number, account_name, bank_code, merchant_tx_ref, sender_name, *, narration: object | None = None, **extra: object) -> _models.PerformBankAccountTransferTheParentAccountResponse:
        """
        Perform bank account transfer from the parent account

        You can use this endpoint to perform bank account transfer.

        Body fields:
            amount (required): The amount to be transferred.
            accountNumber (required): The destination bank account number.
            accountName (required): The name on the account.
            bankCode (required): The code of the recipient bank.
            merchantTxRef (required): Unique reference used to track a transaction from an external process.
            senderName (required): Sender name
            narration: The payment narration
        """
        path = "/v1/transfers/bank"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["accountNumber"] = account_number
        body["accountName"] = account_name
        body["bankCode"] = bank_code
        body["merchantTxRef"] = merchant_tx_ref
        body["senderName"] = sender_name
        if narration is not None:
            body["narration"] = narration
        body.update(extra)
        validate_body("post", "/v1/transfers/bank", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def perform_bank_account_transfer_from_account(self, sub_account_id: str, amount, account_number, account_name, bank_code, merchant_tx_ref, sender_name, *, narration: object | None = None, **extra: object) -> _models.PerformBankAccountTransferFromAccountResponse:
        """
        Perform bank account transfer from a sub account

        You can use this endpoint to perform bank account transfer using a sub account

        Body fields:
            amount (required): The amount to be transferred.
            accountNumber (required): The destination bank account number.
            accountName (required): The name on the account.
            bankCode (required): The code of the recipient bank.
            merchantTxRef (required): Unique reference used to track a transaction from an external process.
            senderName (required): Sender name
            narration: The payment narration
        """
        path = f"/v1/transfers/bank/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["accountNumber"] = account_number
        body["accountName"] = account_name
        body["bankCode"] = bank_code
        body["merchantTxRef"] = merchant_tx_ref
        body["senderName"] = sender_name
        if narration is not None:
            body["narration"] = narration
        body.update(extra)
        validate_body("post", "/v1/transfers/bank/{subAccountId}", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def perform_wallet_transfer_from_the_parent_account(self, amount, receiver_account_id, merchant_tx_ref, *, narration: object | None = None, **extra: object) -> _models.PerformWalletTransferFromTheParentAccountResponse:
        """
        Perform wallet transfer from the parent account

        You can use this endpoint to perform a wallet transfer.

        Body fields:
            amount (required): The amount to be transferred.
            receiverAccountId (required): The receiver's accountId.
            merchantTxRef (required): Unique reference used to track a transaction from an external process.
            narration: The payment narration
        """
        path = "/v1/transfers/wallet"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["receiverAccountId"] = receiver_account_id
        body["merchantTxRef"] = merchant_tx_ref
        if narration is not None:
            body["narration"] = narration
        body.update(extra)
        validate_body("post", "/v1/transfers/wallet", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def perform_wallet_transfer_from_a_sub_account(self, sub_account_id: str, amount, receiver_account_id, merchant_tx_ref, *, narration: object | None = None, **extra: object) -> _models.PerformWalletTransferFromASubAccountResponse:
        """
        Perform wallet transfer from a sub account

        You can use this endpoint to perform a wallet transfer from a sub account

        Body fields:
            amount (required): The amount to be transferred.
            receiverAccountId (required): The receiver's accountId.
            merchantTxRef (required): Unique reference used to track a transaction from an external process.
            narration: The payment narration
        """
        path = f"/v1/transfers/wallet/{sub_account_id}"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["receiverAccountId"] = receiver_account_id
        body["merchantTxRef"] = merchant_tx_ref
        if narration is not None:
            body["narration"] = narration
        body.update(extra)
        validate_body("post", "/v1/transfers/wallet/{subAccountId}", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

