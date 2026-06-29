# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
from __future__ import annotations


from ..http import AsyncNombaClient, NombaClient
from ..validation import validate_body
from .. import models as _models


class Transactions:
    """Sync resource methods for the Transactions group."""

    def __init__(self, client: NombaClient) -> None:
        self._client = client

    def fetch_credit_debit_transactions_on_a_sub_account(self, sub_account_id: str, *, limit: str | None = None, cursor: str | None = None, date_from: str | None = None, date_to: str | None = None, **extra: object) -> _models.FetchCreditDebitTransactionsOnASubAccountResponse:
        """
        Fetch credit/debit transactions on a sub account

        You can use this endpoint to fetch credit/debit transactions on a sub account.
        """
        path = f"/v1/transactions/bank/{sub_account_id}"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if date_from is not None:
            params["dateFrom"] = date_from
        if date_to is not None:
            params["dateTo"] = date_to
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def fetch_credit_debit_transactions_on_the_parent_account(self, *, limit: str | None = None, cursor: str | None = None, date_from: str | None = None, date_to: str | None = None, **extra: object) -> _models.FetchCreditDebitTransactionsOnTheParentAccountResponse:
        """
        Fetch credit/debit transactions on the parent account

        You can use this endpoint to fetch credit/debit transactions on the parent account.
        """
        path = "/v1/transactions/bank"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if date_from is not None:
            params["dateFrom"] = date_from
        if date_to is not None:
            params["dateTo"] = date_to
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def fetch_transactions_on_a_sub_account(self, sub_account_id: str, *, limit: str | None = None, cursor: str | None = None, date_from: str | None = None, date_to: str | None = None, **extra: object) -> _models.FetchTransactionsOnASubAccountResponse:
        """
        Fetch transactions on a sub account

        You can use this endpoint to fetch transactions on a sub account.
        """
        path = f"/v1/transactions/accounts/{sub_account_id}"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if date_from is not None:
            params["dateFrom"] = date_from
        if date_to is not None:
            params["dateTo"] = date_to
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def filter_sub_account_transactions(self, sub_account_id: str, *, limit: str | None = None, cursor: str | None = None, date_from: str | None = None, date_to: str | None = None, transaction_ref: object | None = None, status: object | None = None, source: object | None = None, type_: object | None = None, terminal_id: object | None = None, rrn: object | None = None, merchant_tx_ref: object | None = None, order_reference: object | None = None, order_id: object | None = None, **extra: object) -> _models.FilterSubAccountTransactionsResponse:
        """
        Filter sub account transactions

        You can use this endpoint to filter transactions on a sub account.

        Body fields:
            transactionRef: Transaction ID/Reference
            status: Transaction status
            source: Transaction source
            type: Transaction type
            terminalId: Terminal ID
            rrn: RRN (Retrieval Reference Number)
            merchantTxRef: Merchant transaction reference
            orderReference: Online checkout order reference
            orderId: Online checkout order id
        """
        path = f"/v1/transactions/accounts/{sub_account_id}"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if date_from is not None:
            params["dateFrom"] = date_from
        if date_to is not None:
            params["dateTo"] = date_to
        body: dict[str, object] = {}
        if transaction_ref is not None:
            body["transactionRef"] = transaction_ref
        if status is not None:
            body["status"] = status
        if source is not None:
            body["source"] = source
        if type_ is not None:
            body["type"] = type_
        if terminal_id is not None:
            body["terminalId"] = terminal_id
        if rrn is not None:
            body["rrn"] = rrn
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if order_reference is not None:
            body["orderReference"] = order_reference
        if order_id is not None:
            body["orderId"] = order_id
        body.update(extra)
        validate_body("post", "/v1/transactions/accounts/{subAccountId}", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def fetch_transactions_on_the_parent_account(self, *, limit: str | None = None, cursor: str | None = None, date_from: str | None = None, date_to: str | None = None, **extra: object) -> _models.FetchTransactionsOnTheParentAccountResponse:
        """
        Fetch transactions on the parent account

        You can use this endpoint to fetch transactions on the parent account.
        """
        path = "/v1/transactions/accounts"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if date_from is not None:
            params["dateFrom"] = date_from
        if date_to is not None:
            params["dateTo"] = date_to
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def filter_parent_account_transactions(self, *, limit: str | None = None, cursor: str | None = None, date_from: str | None = None, date_to: str | None = None, transaction_ref: object | None = None, status: object | None = None, source: object | None = None, type_: object | None = None, terminal_id: object | None = None, rrn: object | None = None, merchant_tx_ref: object | None = None, order_reference: object | None = None, order_id: object | None = None, **extra: object) -> _models.FilterParentAccountTransactionsResponse:
        """
        Filter parent account transactions

        You can use this endpoint to filter transactions on the parent account.

        Body fields:
            transactionRef: Transaction ID/Reference
            status: Transaction status
            source: Transaction source
            type: Transaction type
            terminalId: Terminal ID
            rrn: RRN (Retrieval Reference Number)
            merchantTxRef: Merchant transaction reference
            orderReference: Online checkout order reference
            orderId: Online checkout order id
        """
        path = "/v1/transactions/accounts"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if date_from is not None:
            params["dateFrom"] = date_from
        if date_to is not None:
            params["dateTo"] = date_to
        body: dict[str, object] = {}
        if transaction_ref is not None:
            body["transactionRef"] = transaction_ref
        if status is not None:
            body["status"] = status
        if source is not None:
            body["source"] = source
        if type_ is not None:
            body["type"] = type_
        if terminal_id is not None:
            body["terminalId"] = terminal_id
        if rrn is not None:
            body["rrn"] = rrn
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if order_reference is not None:
            body["orderReference"] = order_reference
        if order_id is not None:
            body["orderId"] = order_id
        body.update(extra)
        validate_body("post", "/v1/transactions/accounts", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def fetch_a_single_transaction_on_a_sub_account(self, sub_account_id: str, *, transaction_ref: str | None = None, merchant_tx_ref: str | None = None, order_reference: str | None = None, order_id: str | None = None, **extra: object) -> _models.FetchASingleTransactionOnASubAccountResponse:
        """
        Fetch a single transaction on a sub account

        You can use this endpoint to fetch a single transaction on a sub account
        """
        path = f"/v1/transactions/accounts/{sub_account_id}/single"
        params: dict[str, object] = {}
        if transaction_ref is not None:
            params["transactionRef"] = transaction_ref
        if merchant_tx_ref is not None:
            params["merchantTxRef"] = merchant_tx_ref
        if order_reference is not None:
            params["orderReference"] = order_reference
        if order_id is not None:
            params["orderId"] = order_id
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def fetch_a_single_transaction_on_the_parent_account(self, *, transaction_ref: str | None = None, merchant_tx_ref: str | None = None, order_reference: str | None = None, order_id: str | None = None, **extra: object) -> _models.FetchASingleTransactionOnTheParentAccountResponse:
        """
        Fetch a single transaction on the parent account

        You can use this endpoint to fetch a single transaction on the parent account.
        """
        path = "/v1/transactions/accounts/single"
        params: dict[str, object] = {}
        if transaction_ref is not None:
            params["transactionRef"] = transaction_ref
        if merchant_tx_ref is not None:
            params["merchantTxRef"] = merchant_tx_ref
        if order_reference is not None:
            params["orderReference"] = order_reference
        if order_id is not None:
            params["orderId"] = order_id
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def confirm_a_transaction_s_status_by_session_id(self, session_id: str, **extra: object) -> _models.ConfirmATransactionSStatusBySessionIdResponse:
        """
        Confirm a transaction's status by sessionId

        This endpoint is for fetching (requerying) a transaction status.
        """
        path = f"/v1/transactions/requery/{session_id}"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]



class AsyncTransactions:
    """Async resource methods for the Transactions group."""

    def __init__(self, client: AsyncNombaClient) -> None:
        self._client = client

    async def fetch_credit_debit_transactions_on_a_sub_account(self, sub_account_id: str, *, limit: str | None = None, cursor: str | None = None, date_from: str | None = None, date_to: str | None = None, **extra: object) -> _models.FetchCreditDebitTransactionsOnASubAccountResponse:
        """
        Fetch credit/debit transactions on a sub account

        You can use this endpoint to fetch credit/debit transactions on a sub account.
        """
        path = f"/v1/transactions/bank/{sub_account_id}"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if date_from is not None:
            params["dateFrom"] = date_from
        if date_to is not None:
            params["dateTo"] = date_to
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def fetch_credit_debit_transactions_on_the_parent_account(self, *, limit: str | None = None, cursor: str | None = None, date_from: str | None = None, date_to: str | None = None, **extra: object) -> _models.FetchCreditDebitTransactionsOnTheParentAccountResponse:
        """
        Fetch credit/debit transactions on the parent account

        You can use this endpoint to fetch credit/debit transactions on the parent account.
        """
        path = "/v1/transactions/bank"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if date_from is not None:
            params["dateFrom"] = date_from
        if date_to is not None:
            params["dateTo"] = date_to
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def fetch_transactions_on_a_sub_account(self, sub_account_id: str, *, limit: str | None = None, cursor: str | None = None, date_from: str | None = None, date_to: str | None = None, **extra: object) -> _models.FetchTransactionsOnASubAccountResponse:
        """
        Fetch transactions on a sub account

        You can use this endpoint to fetch transactions on a sub account.
        """
        path = f"/v1/transactions/accounts/{sub_account_id}"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if date_from is not None:
            params["dateFrom"] = date_from
        if date_to is not None:
            params["dateTo"] = date_to
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def filter_sub_account_transactions(self, sub_account_id: str, *, limit: str | None = None, cursor: str | None = None, date_from: str | None = None, date_to: str | None = None, transaction_ref: object | None = None, status: object | None = None, source: object | None = None, type_: object | None = None, terminal_id: object | None = None, rrn: object | None = None, merchant_tx_ref: object | None = None, order_reference: object | None = None, order_id: object | None = None, **extra: object) -> _models.FilterSubAccountTransactionsResponse:
        """
        Filter sub account transactions

        You can use this endpoint to filter transactions on a sub account.

        Body fields:
            transactionRef: Transaction ID/Reference
            status: Transaction status
            source: Transaction source
            type: Transaction type
            terminalId: Terminal ID
            rrn: RRN (Retrieval Reference Number)
            merchantTxRef: Merchant transaction reference
            orderReference: Online checkout order reference
            orderId: Online checkout order id
        """
        path = f"/v1/transactions/accounts/{sub_account_id}"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if date_from is not None:
            params["dateFrom"] = date_from
        if date_to is not None:
            params["dateTo"] = date_to
        body: dict[str, object] = {}
        if transaction_ref is not None:
            body["transactionRef"] = transaction_ref
        if status is not None:
            body["status"] = status
        if source is not None:
            body["source"] = source
        if type_ is not None:
            body["type"] = type_
        if terminal_id is not None:
            body["terminalId"] = terminal_id
        if rrn is not None:
            body["rrn"] = rrn
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if order_reference is not None:
            body["orderReference"] = order_reference
        if order_id is not None:
            body["orderId"] = order_id
        body.update(extra)
        validate_body("post", "/v1/transactions/accounts/{subAccountId}", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def fetch_transactions_on_the_parent_account(self, *, limit: str | None = None, cursor: str | None = None, date_from: str | None = None, date_to: str | None = None, **extra: object) -> _models.FetchTransactionsOnTheParentAccountResponse:
        """
        Fetch transactions on the parent account

        You can use this endpoint to fetch transactions on the parent account.
        """
        path = "/v1/transactions/accounts"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if date_from is not None:
            params["dateFrom"] = date_from
        if date_to is not None:
            params["dateTo"] = date_to
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def filter_parent_account_transactions(self, *, limit: str | None = None, cursor: str | None = None, date_from: str | None = None, date_to: str | None = None, transaction_ref: object | None = None, status: object | None = None, source: object | None = None, type_: object | None = None, terminal_id: object | None = None, rrn: object | None = None, merchant_tx_ref: object | None = None, order_reference: object | None = None, order_id: object | None = None, **extra: object) -> _models.FilterParentAccountTransactionsResponse:
        """
        Filter parent account transactions

        You can use this endpoint to filter transactions on the parent account.

        Body fields:
            transactionRef: Transaction ID/Reference
            status: Transaction status
            source: Transaction source
            type: Transaction type
            terminalId: Terminal ID
            rrn: RRN (Retrieval Reference Number)
            merchantTxRef: Merchant transaction reference
            orderReference: Online checkout order reference
            orderId: Online checkout order id
        """
        path = "/v1/transactions/accounts"
        params: dict[str, object] = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if date_from is not None:
            params["dateFrom"] = date_from
        if date_to is not None:
            params["dateTo"] = date_to
        body: dict[str, object] = {}
        if transaction_ref is not None:
            body["transactionRef"] = transaction_ref
        if status is not None:
            body["status"] = status
        if source is not None:
            body["source"] = source
        if type_ is not None:
            body["type"] = type_
        if terminal_id is not None:
            body["terminalId"] = terminal_id
        if rrn is not None:
            body["rrn"] = rrn
        if merchant_tx_ref is not None:
            body["merchantTxRef"] = merchant_tx_ref
        if order_reference is not None:
            body["orderReference"] = order_reference
        if order_id is not None:
            body["orderId"] = order_id
        body.update(extra)
        validate_body("post", "/v1/transactions/accounts", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def fetch_a_single_transaction_on_a_sub_account(self, sub_account_id: str, *, transaction_ref: str | None = None, merchant_tx_ref: str | None = None, order_reference: str | None = None, order_id: str | None = None, **extra: object) -> _models.FetchASingleTransactionOnASubAccountResponse:
        """
        Fetch a single transaction on a sub account

        You can use this endpoint to fetch a single transaction on a sub account
        """
        path = f"/v1/transactions/accounts/{sub_account_id}/single"
        params: dict[str, object] = {}
        if transaction_ref is not None:
            params["transactionRef"] = transaction_ref
        if merchant_tx_ref is not None:
            params["merchantTxRef"] = merchant_tx_ref
        if order_reference is not None:
            params["orderReference"] = order_reference
        if order_id is not None:
            params["orderId"] = order_id
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def fetch_a_single_transaction_on_the_parent_account(self, *, transaction_ref: str | None = None, merchant_tx_ref: str | None = None, order_reference: str | None = None, order_id: str | None = None, **extra: object) -> _models.FetchASingleTransactionOnTheParentAccountResponse:
        """
        Fetch a single transaction on the parent account

        You can use this endpoint to fetch a single transaction on the parent account.
        """
        path = "/v1/transactions/accounts/single"
        params: dict[str, object] = {}
        if transaction_ref is not None:
            params["transactionRef"] = transaction_ref
        if merchant_tx_ref is not None:
            params["merchantTxRef"] = merchant_tx_ref
        if order_reference is not None:
            params["orderReference"] = order_reference
        if order_id is not None:
            params["orderId"] = order_id
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def confirm_a_transaction_s_status_by_session_id(self, session_id: str, **extra: object) -> _models.ConfirmATransactionSStatusBySessionIdResponse:
        """
        Confirm a transaction's status by sessionId

        This endpoint is for fetching (requerying) a transaction status.
        """
        path = f"/v1/transactions/requery/{session_id}"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

