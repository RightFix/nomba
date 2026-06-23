from __future__ import annotations

from .http import AsyncNombaClient, NombaClient
from .resources import (
    Accounts,
    AirtimeData,
    AsyncAccounts,
    AsyncAirtimeData,
    AsyncCableTv,
    AsyncCharge,
    AsyncCheckout,
    AsyncElectricity,
    AsyncTerminals,
    AsyncTransactions,
    AsyncTransfers,
    AsyncVirtualAccounts,
    CableTv,
    Charge,
    Checkout,
    Electricity,
    Terminals,
    Transactions,
    Transfers,
    VirtualAccounts,
)
from .flows import CardPaymentFlow, AsyncCardPaymentFlow


class Nomba:
    """
    High-level entry point for the Nomba SDK. Covers every endpoint in
    Nomba's published OpenAPI spec.

    Example:
        from nomba import Nomba

        nomba = Nomba(
            client_id="...",
            client_secret="...",
            account_id="...",
            sandbox=True,
        )

        account = nomba.virtual_accounts.create_virtual_account(
            account_ref="ref-123",
            account_name="Jane Doe",
        )

    Resource groups:
        accounts, virtual_accounts, checkout, charge, transfers,
        terminals, transactions, airtime_data, cabletv, electricity
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        account_id: str,
        *,
        sandbox: bool = False,
        timeout: float = 30.0,
    ) -> None:
        self.client = NombaClient(
            client_id=client_id,
            client_secret=client_secret,
            account_id=account_id,
            sandbox=sandbox,
            timeout=timeout,
        )
        self.accounts = Accounts(self.client)
        self.virtual_accounts = VirtualAccounts(self.client)
        self.checkout = Checkout(self.client)
        self.charge = Charge(self.client)
        self.transfers = Transfers(self.client)
        self.terminals = Terminals(self.client)
        self.transactions = Transactions(self.client)
        self.airtime_data = AirtimeData(self.client)
        self.cabletv = CableTv(self.client)
        self.electricity = Electricity(self.client)

    def close(self) -> None:
        self.client.close()

    def card_payment(self, order_reference: str) -> "CardPaymentFlow":
        """Start a guided card-payment flow for an existing checkout order.
        See `nomba.flows.CardPaymentFlow` for the full step-by-step API."""
        from .flows import CardPaymentFlow

        return CardPaymentFlow(self.charge, order_reference=order_reference)

    def __enter__(self) -> "Nomba":
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()


class AsyncNomba:
    """
    Async high-level entry point for the Nomba SDK (uses httpx.AsyncClient).
    Covers every endpoint in Nomba's published OpenAPI spec.

    Example:
        from nomba import AsyncNomba

        async def main():
            nomba = AsyncNomba(
                client_id="...",
                client_secret="...",
                account_id="...",
                sandbox=True,
            )
            account = await nomba.virtual_accounts.create_virtual_account(
                account_ref="ref-123",
                account_name="Jane Doe",
            )
            await nomba.close()
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        account_id: str,
        *,
        sandbox: bool = False,
        timeout: float = 30.0,
    ) -> None:
        self.client = AsyncNombaClient(
            client_id=client_id,
            client_secret=client_secret,
            account_id=account_id,
            sandbox=sandbox,
            timeout=timeout,
        )
        self.accounts = AsyncAccounts(self.client)
        self.virtual_accounts = AsyncVirtualAccounts(self.client)
        self.checkout = AsyncCheckout(self.client)
        self.charge = AsyncCharge(self.client)
        self.transfers = AsyncTransfers(self.client)
        self.terminals = AsyncTerminals(self.client)
        self.transactions = AsyncTransactions(self.client)
        self.airtime_data = AsyncAirtimeData(self.client)
        self.cabletv = AsyncCableTv(self.client)
        self.electricity = AsyncElectricity(self.client)

    async def close(self) -> None:
        await self.client.close()

    def card_payment(self, order_reference: str) -> "AsyncCardPaymentFlow":
        """Start a guided async card-payment flow for an existing checkout
        order. See `nomba.flows.AsyncCardPaymentFlow` for the full API."""
        from .flows import AsyncCardPaymentFlow

        return AsyncCardPaymentFlow(self.charge, order_reference=order_reference)

    async def __aenter__(self) -> "AsyncNomba":
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        await self.close()
