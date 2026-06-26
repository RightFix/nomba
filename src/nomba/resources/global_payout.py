# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
from __future__ import annotations

from typing import Any

from ..http import AsyncNombaClient, NombaClient
from ..validation import validate_body
from .. import models as _models


class GlobalPayout:
    """Sync resource methods for the GlobalPayout group."""

    def __init__(self, client: NombaClient) -> None:
        self._client = client

    def authorize_transfer(self, amount, source_currency, destination_currency, receiver_name, source_country_iso_code, destination_country_iso_code, auth_code, payment_method, account_type, *, account_number: object | None = None, institution_code: object | None = None, institution_name: object | None = None, bank_account_type: object | None = None, purpose_of_payment: object | None = None, narration: object | None = None, locked_exchange_rate_id: object | None = None, bank_address: object | None = None, bank_city: object | None = None, bank_state: object | None = None, bank_zip_code: object | None = None, beneficiary: object | None = None, **extra: object) -> _models.AuthorizeTransferResponse:
        """

        Initiate and authorize a cross-border transfer. Manages the complete transfer lifecycle from initiation to final authorization. Supports BANK, MobileMoney, INTERAC, FASTER_PAYMENTS, SEPA, ACH, and WIRE payment methods.

        Body fields:
            amount (required): 
            sourceCurrency (required): 
            destinationCurrency (required): 
            receiverName (required): 
            sourceCountryIsoCode (required): 
            destinationCountryIsoCode (required): 
            authCode (required): 
            paymentMethod (required): Payment rail. Determines which additional fields are required. Use Fetch Payment Methods with code or name to get method-specific requirements.
            accountType (required): Required account type of the recipient. Select one of the values returned in accountTypes from Fetch Payment Methods. ACH supports only INDIVIDUAL; WIRE supports INDIVIDUAL and CORPORATE.
            accountNumber: Account number, IBAN, or phone number for MobileMoney. Required for BANK, MobileMoney, FASTER_PAYMENTS, SEPA.
            institutionCode: Routing code. Bank code from /bank/providers for BANK (DRC). Sort code for FASTER_PAYMENTS, SWIFT/BIC for SEPA, institution number for BANK (Canada).
            institutionName: Bank or provider display name. Use displayName from List Institution Providers.
            bankAccountType: Recipient bank account type. Required for ACH and WIRE. Select one of the values returned in bankAccountTypes from Fetch Payment Methods.
            purposeOfPayment: Reason for the transfer. Required for ACH, WIRE, and SEPA. Select one of the values returned in purposeOfPayments from Fetch Payment Methods; do not send arbitrary text.
            narration: 
            lockedExchangeRateId: Optional locked exchange rate ID from Convert Money. Use this when you want to lock the exchange rate and destination amount before authorizing.
            bankAddress: Bank street address. Required for United States WIRE.
            bankCity: Bank city. Required for United States WIRE.
            bankState: Bank state. Required for United States WIRE.
            bankZipCode: Bank ZIP code. Required for United States WIRE.
            beneficiary: Required for INTERAC; partially required for BANK (Canada).
        """
        path = f"/v1/global-payout/transfer/authorize"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["sourceCurrency"] = source_currency
        body["destinationCurrency"] = destination_currency
        body["receiverName"] = receiver_name
        body["sourceCountryIsoCode"] = source_country_iso_code
        body["destinationCountryIsoCode"] = destination_country_iso_code
        body["authCode"] = auth_code
        body["paymentMethod"] = payment_method
        body["accountType"] = account_type
        if account_number is not None:
            body["accountNumber"] = account_number
        if institution_code is not None:
            body["institutionCode"] = institution_code
        if institution_name is not None:
            body["institutionName"] = institution_name
        if bank_account_type is not None:
            body["bankAccountType"] = bank_account_type
        if purpose_of_payment is not None:
            body["purposeOfPayment"] = purpose_of_payment
        if narration is not None:
            body["narration"] = narration
        if locked_exchange_rate_id is not None:
            body["lockedExchangeRateId"] = locked_exchange_rate_id
        if bank_address is not None:
            body["bankAddress"] = bank_address
        if bank_city is not None:
            body["bankCity"] = bank_city
        if bank_state is not None:
            body["bankState"] = bank_state
        if bank_zip_code is not None:
            body["bankZipCode"] = bank_zip_code
        if beneficiary is not None:
            body["beneficiary"] = beneficiary
        body.update(extra)
        validate_body("post", "/v1/global-payout/transfer/authorize", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def authorize_exchange(self, amount, source_currency, destination_currency, sender_name, receiver_name, source_country_iso_code, destination_country_iso_code, auth_code, *, narration: object | None = None, locked_exchange_rate_id: object | None = None, **extra: object) -> _models.AuthorizeExchangeResponse:
        """

        Transfer funds between your own accounts in different currencies.

        Body fields:
            amount (required): 
            sourceCurrency (required): 
            destinationCurrency (required): 
            senderName (required): 
            receiverName (required): 
            sourceCountryIsoCode (required): 
            destinationCountryIsoCode (required): 
            authCode (required): 
            narration: 
            lockedExchangeRateId: The exchangeRateId from a prior Fetch Exchange Rates call. When provided, the exchange is fulfilled at that exact rate.
        """
        path = f"/v1/global-payout/exchange/authorize"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["sourceCurrency"] = source_currency
        body["destinationCurrency"] = destination_currency
        body["senderName"] = sender_name
        body["receiverName"] = receiver_name
        body["sourceCountryIsoCode"] = source_country_iso_code
        body["destinationCountryIsoCode"] = destination_country_iso_code
        body["authCode"] = auth_code
        if narration is not None:
            body["narration"] = narration
        if locked_exchange_rate_id is not None:
            body["lockedExchangeRateId"] = locked_exchange_rate_id
        body.update(extra)
        validate_body("post", "/v1/global-payout/exchange/authorize", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def convert_money(self, amount, currency, destination_currency, transaction_type, source_country_iso_code, **extra: object) -> _models.ConvertMoneyResponse:
        """

        Calculate a currency conversion and lock an exchange rate before initiating a transfer.

        Body fields:
            amount (required): 
            currency (required): ISO 4217 source currency code.
            destinationCurrency (required): ISO 4217 destination currency code.
            transactionType (required): 
            sourceCountryIsoCode (required): 
        """
        path = f"/v1/global-payout/money/convert"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["currency"] = currency
        body["destinationCurrency"] = destination_currency
        body["transactionType"] = transaction_type
        body["sourceCountryIsoCode"] = source_country_iso_code
        body.update(extra)
        validate_body("post", "/v1/global-payout/money/convert", body)
        return self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    def fetch_exchange_rates(self, *, from_: str, to: str, region: str | None = None, **extra: object) -> _models.FetchExchangeRatesResponse:
        """

        Retrieve the latest exchange rates for a currency pair before initiating a transfer.
        """
        path = f"/v1/global-payout/exchange-rates"
        params: dict[str, object] = {}
        if from_ is not None:
            params["from"] = from_
        if to is not None:
            params["to"] = to
        if region is not None:
            params["region"] = region
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def fetch_global_payout_transaction(self, transaction_id: str, **extra: object) -> _models.FetchGlobalPayoutTransactionResponse:
        """

        Track the status of any Global Payout transaction using its transaction ID.
        """
        path = f"/v1/global-payout/transactions/{transaction_id}"
        params = None
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def fetch_payment_methods(self, *, code: str | None = None, name: str | None = None, **extra: object) -> _models.FetchPaymentMethodsResponse:
        """

        Returns all supported payment methods and their method-specific requirements. Filter by code or name to retrieve a specific method.
        """
        path = f"/v1/global-payout/payment-methods"
        params: dict[str, object] = {}
        if code is not None:
            params["code"] = code
        if name is not None:
            params["name"] = name
        return self._client.get(path, params=params)  # type: ignore[return-value]

    def list_institution_providers(self, *, is_mobile_money: str | None = None, country_iso_code: str | None = None, **extra: object) -> _models.ListInstitutionProvidersResponse:
        """

        Returns available bank, institution, or mobile money providers. Use isMobileMoney=false for bank/institution providers and isMobileMoney=true for mobile money providers. Use code as institutionCode and displayName as institutionName in Authorize Transfer.
        """
        path = f"/v1/global-payout/bank/providers"
        params: dict[str, object] = {}
        if is_mobile_money is not None:
            params["isMobileMoney"] = is_mobile_money
        if country_iso_code is not None:
            params["countryIsoCode"] = country_iso_code
        return self._client.get(path, params=params)  # type: ignore[return-value]



class AsyncGlobalPayout:
    """Async resource methods for the GlobalPayout group."""

    def __init__(self, client: AsyncNombaClient) -> None:
        self._client = client

    async def authorize_transfer(self, amount, source_currency, destination_currency, receiver_name, source_country_iso_code, destination_country_iso_code, auth_code, payment_method, account_type, *, account_number: object | None = None, institution_code: object | None = None, institution_name: object | None = None, bank_account_type: object | None = None, purpose_of_payment: object | None = None, narration: object | None = None, locked_exchange_rate_id: object | None = None, bank_address: object | None = None, bank_city: object | None = None, bank_state: object | None = None, bank_zip_code: object | None = None, beneficiary: object | None = None, **extra: object) -> _models.AuthorizeTransferResponse:
        """

        Initiate and authorize a cross-border transfer. Manages the complete transfer lifecycle from initiation to final authorization. Supports BANK, MobileMoney, INTERAC, FASTER_PAYMENTS, SEPA, ACH, and WIRE payment methods.

        Body fields:
            amount (required): 
            sourceCurrency (required): 
            destinationCurrency (required): 
            receiverName (required): 
            sourceCountryIsoCode (required): 
            destinationCountryIsoCode (required): 
            authCode (required): 
            paymentMethod (required): Payment rail. Determines which additional fields are required. Use Fetch Payment Methods with code or name to get method-specific requirements.
            accountType (required): Required account type of the recipient. Select one of the values returned in accountTypes from Fetch Payment Methods. ACH supports only INDIVIDUAL; WIRE supports INDIVIDUAL and CORPORATE.
            accountNumber: Account number, IBAN, or phone number for MobileMoney. Required for BANK, MobileMoney, FASTER_PAYMENTS, SEPA.
            institutionCode: Routing code. Bank code from /bank/providers for BANK (DRC). Sort code for FASTER_PAYMENTS, SWIFT/BIC for SEPA, institution number for BANK (Canada).
            institutionName: Bank or provider display name. Use displayName from List Institution Providers.
            bankAccountType: Recipient bank account type. Required for ACH and WIRE. Select one of the values returned in bankAccountTypes from Fetch Payment Methods.
            purposeOfPayment: Reason for the transfer. Required for ACH, WIRE, and SEPA. Select one of the values returned in purposeOfPayments from Fetch Payment Methods; do not send arbitrary text.
            narration: 
            lockedExchangeRateId: Optional locked exchange rate ID from Convert Money. Use this when you want to lock the exchange rate and destination amount before authorizing.
            bankAddress: Bank street address. Required for United States WIRE.
            bankCity: Bank city. Required for United States WIRE.
            bankState: Bank state. Required for United States WIRE.
            bankZipCode: Bank ZIP code. Required for United States WIRE.
            beneficiary: Required for INTERAC; partially required for BANK (Canada).
        """
        path = f"/v1/global-payout/transfer/authorize"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["sourceCurrency"] = source_currency
        body["destinationCurrency"] = destination_currency
        body["receiverName"] = receiver_name
        body["sourceCountryIsoCode"] = source_country_iso_code
        body["destinationCountryIsoCode"] = destination_country_iso_code
        body["authCode"] = auth_code
        body["paymentMethod"] = payment_method
        body["accountType"] = account_type
        if account_number is not None:
            body["accountNumber"] = account_number
        if institution_code is not None:
            body["institutionCode"] = institution_code
        if institution_name is not None:
            body["institutionName"] = institution_name
        if bank_account_type is not None:
            body["bankAccountType"] = bank_account_type
        if purpose_of_payment is not None:
            body["purposeOfPayment"] = purpose_of_payment
        if narration is not None:
            body["narration"] = narration
        if locked_exchange_rate_id is not None:
            body["lockedExchangeRateId"] = locked_exchange_rate_id
        if bank_address is not None:
            body["bankAddress"] = bank_address
        if bank_city is not None:
            body["bankCity"] = bank_city
        if bank_state is not None:
            body["bankState"] = bank_state
        if bank_zip_code is not None:
            body["bankZipCode"] = bank_zip_code
        if beneficiary is not None:
            body["beneficiary"] = beneficiary
        body.update(extra)
        validate_body("post", "/v1/global-payout/transfer/authorize", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def authorize_exchange(self, amount, source_currency, destination_currency, sender_name, receiver_name, source_country_iso_code, destination_country_iso_code, auth_code, *, narration: object | None = None, locked_exchange_rate_id: object | None = None, **extra: object) -> _models.AuthorizeExchangeResponse:
        """

        Transfer funds between your own accounts in different currencies.

        Body fields:
            amount (required): 
            sourceCurrency (required): 
            destinationCurrency (required): 
            senderName (required): 
            receiverName (required): 
            sourceCountryIsoCode (required): 
            destinationCountryIsoCode (required): 
            authCode (required): 
            narration: 
            lockedExchangeRateId: The exchangeRateId from a prior Fetch Exchange Rates call. When provided, the exchange is fulfilled at that exact rate.
        """
        path = f"/v1/global-payout/exchange/authorize"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["sourceCurrency"] = source_currency
        body["destinationCurrency"] = destination_currency
        body["senderName"] = sender_name
        body["receiverName"] = receiver_name
        body["sourceCountryIsoCode"] = source_country_iso_code
        body["destinationCountryIsoCode"] = destination_country_iso_code
        body["authCode"] = auth_code
        if narration is not None:
            body["narration"] = narration
        if locked_exchange_rate_id is not None:
            body["lockedExchangeRateId"] = locked_exchange_rate_id
        body.update(extra)
        validate_body("post", "/v1/global-payout/exchange/authorize", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def convert_money(self, amount, currency, destination_currency, transaction_type, source_country_iso_code, **extra: object) -> _models.ConvertMoneyResponse:
        """

        Calculate a currency conversion and lock an exchange rate before initiating a transfer.

        Body fields:
            amount (required): 
            currency (required): ISO 4217 source currency code.
            destinationCurrency (required): ISO 4217 destination currency code.
            transactionType (required): 
            sourceCountryIsoCode (required): 
        """
        path = f"/v1/global-payout/money/convert"
        params = None
        body: dict[str, object] = {}
        body["amount"] = amount
        body["currency"] = currency
        body["destinationCurrency"] = destination_currency
        body["transactionType"] = transaction_type
        body["sourceCountryIsoCode"] = source_country_iso_code
        body.update(extra)
        validate_body("post", "/v1/global-payout/money/convert", body)
        return await self._client.post(path, json=body, params=params)  # type: ignore[return-value]

    async def fetch_exchange_rates(self, *, from_: str, to: str, region: str | None = None, **extra: object) -> _models.FetchExchangeRatesResponse:
        """

        Retrieve the latest exchange rates for a currency pair before initiating a transfer.
        """
        path = f"/v1/global-payout/exchange-rates"
        params: dict[str, object] = {}
        if from_ is not None:
            params["from"] = from_
        if to is not None:
            params["to"] = to
        if region is not None:
            params["region"] = region
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def fetch_global_payout_transaction(self, transaction_id: str, **extra: object) -> _models.FetchGlobalPayoutTransactionResponse:
        """

        Track the status of any Global Payout transaction using its transaction ID.
        """
        path = f"/v1/global-payout/transactions/{transaction_id}"
        params = None
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def fetch_payment_methods(self, *, code: str | None = None, name: str | None = None, **extra: object) -> _models.FetchPaymentMethodsResponse:
        """

        Returns all supported payment methods and their method-specific requirements. Filter by code or name to retrieve a specific method.
        """
        path = f"/v1/global-payout/payment-methods"
        params: dict[str, object] = {}
        if code is not None:
            params["code"] = code
        if name is not None:
            params["name"] = name
        return await self._client.get(path, params=params)  # type: ignore[return-value]

    async def list_institution_providers(self, *, is_mobile_money: str | None = None, country_iso_code: str | None = None, **extra: object) -> _models.ListInstitutionProvidersResponse:
        """

        Returns available bank, institution, or mobile money providers. Use isMobileMoney=false for bank/institution providers and isMobileMoney=true for mobile money providers. Use code as institutionCode and displayName as institutionName in Authorize Transfer.
        """
        path = f"/v1/global-payout/bank/providers"
        params: dict[str, object] = {}
        if is_mobile_money is not None:
            params["isMobileMoney"] = is_mobile_money
        if country_iso_code is not None:
            params["countryIsoCode"] = country_iso_code
        return await self._client.get(path, params=params)  # type: ignore[return-value]

