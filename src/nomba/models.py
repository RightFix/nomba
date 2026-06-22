# This file is auto-generated from Nomba's OpenAPI spec. Do not edit by hand;
# regenerate via scripts/generate_resources.py instead.
#
# These TypedDicts describe the shape of each endpoint's response for
# editor autocomplete / type checking. They cost nothing at runtime --
# methods still return plain dicts; TypedDict is purely a type hint.
from __future__ import annotations

from typing import Any, TypedDict


class ListAllAccountsResponse(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class CreateASubAccountData(TypedDict, total=False):
    createdAt: str
    accountId: str
    accountHolderId: str
    accountRef: str
    phoneNumber: str
    email: str
    bvn: str
    status: str
    type: str
    accountName: str
    currency: str
    callbackUrl: str
    expiryDate: str

class CreateASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: CreateASubAccountData

class FetchAccountDetailsData(TypedDict, total=False):
    createdAt: str
    accountId: str
    accountHolderId: str
    accountRef: str
    bvn: str
    status: str
    type: str
    accountName: str
    currency: str
    banks: list[dict[str, Any]]

class FetchAccountDetailsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchAccountDetailsData

class FetchParentAccountDetailsData(TypedDict, total=False):
    createdAt: str
    accountId: str
    accountHolderId: str
    accountRef: str
    bvn: str
    status: str
    type: str
    accountName: str
    currency: str
    banks: list[dict[str, Any]]

class FetchParentAccountDetailsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchParentAccountDetailsData

class FetchAccountBalanceData(TypedDict, total=False):
    amount: str
    currency: str
    timeCreated: str

class FetchAccountBalanceResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchAccountBalanceData

class FetchParentAccountBalanceData(TypedDict, total=False):
    amount: str
    currency: str
    timeCreated: str

class FetchParentAccountBalanceResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchParentAccountBalanceData

class SuspendAnAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: dict[str, Any]

class ReactivateASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: dict[str, Any]

class FetchTerminalsAssignedToAnAccountData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FetchTerminalsAssignedToAnAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchTerminalsAssignedToAnAccountData

class FetchTerminalsAssignedToTheParentAccountData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FetchTerminalsAssignedToTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchTerminalsAssignedToTheParentAccountData

class UpdateAccessToAccountData(TypedDict, total=False):
    message: str
    data: dict[str, Any]

class UpdateAccessToAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: UpdateAccessToAccountData

class CreateVirtualAccountData(TypedDict, total=False):
    createdAt: str
    accountHolderId: str
    accountRef: str
    bvn: str
    accountName: str
    bankName: str
    bankAccountNumber: str
    bankAccountName: str
    currency: str
    callbackUrl: str
    expired: bool

class CreateVirtualAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: CreateVirtualAccountData

class FilterVirtualAccountsData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FilterVirtualAccountsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FilterVirtualAccountsData

class UpdateAVirtualAccountData(TypedDict, total=False):
    updated: bool

class UpdateAVirtualAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: UpdateAVirtualAccountData

class FetchAVirtualAccountData(TypedDict, total=False):
    createdAt: str
    accountHolderId: str
    accountRef: str
    bvn: str
    accountName: str
    bankName: str
    bankAccountNumber: str
    bankAccountName: str
    currency: str
    callbackUrl: str
    expired: bool

class FetchAVirtualAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchAVirtualAccountData

class ExpireAVirtualAccountData(TypedDict, total=False):
    expired: bool

class ExpireAVirtualAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: ExpireAVirtualAccountData

class CreateAnOnlineCheckoutOrderData(TypedDict, total=False):
    checkoutLink: str
    orderReference: str

class CreateAnOnlineCheckoutOrderResponse(TypedDict, total=False):
    code: str
    description: str
    data: CreateAnOnlineCheckoutOrderData

class ChargeCustomerWithTokenizedCardDataData(TypedDict, total=False):
    status: bool
    message: str

class ChargeCustomerWithTokenizedCardDataResponse(TypedDict, total=False):
    code: str
    description: str
    data: ChargeCustomerWithTokenizedCardDataData

class ListAllTokenizedCardsForMerchantData(TypedDict, total=False):
    nextPage: str
    tokenizedCardDataList: list[dict[str, Any]]

class ListAllTokenizedCardsForMerchantResponse(TypedDict, total=False):
    code: str
    description: str
    data: ListAllTokenizedCardsForMerchantData

class UpdateTokenizedCardDataData(TypedDict, total=False):
    status: bool
    message: str
    tokenizedCardData: Any

class UpdateTokenizedCardDataResponse(TypedDict, total=False):
    code: str
    description: str
    data: UpdateTokenizedCardDataData

class DeleteTokenizedCardDataData(TypedDict, total=False):
    status: bool
    message: str

class DeleteTokenizedCardDataResponse(TypedDict, total=False):
    code: str
    description: str
    data: DeleteTokenizedCardDataData

class FetchACheckoutTransactionData(TypedDict, total=False):
    success: bool
    message: str
    order: dict[str, Any]
    transactionDetails: dict[str, Any]
    transferDetails: dict[str, Any]
    cardDetails: dict[str, Any]

class FetchACheckoutTransactionResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchACheckoutTransactionData

class FetchCheckoutOrderDetailsData(TypedDict, total=False):
    order: dict[str, Any]
    hasSavedCards: bool
    base64EncodedRsaPublicKey: str

class FetchCheckoutOrderDetailsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchCheckoutOrderDetailsData

class SubmitCustomerCardDetailsData(TypedDict, total=False):
    status: bool
    message: str
    responseCode: str
    transactionId: str
    secureAuthenticationData: dict[str, Any]

class SubmitCustomerCardDetailsResponse(TypedDict, total=False):
    code: str
    description: str
    data: SubmitCustomerCardDetailsData

class SubmitCustomerPaymentOtpData(TypedDict, total=False):
    status: bool
    message: str

class SubmitCustomerPaymentOtpResponse(TypedDict, total=False):
    code: str
    description: str
    data: SubmitCustomerPaymentOtpData

class ResendCustomerPaymentOtpData(TypedDict, total=False):
    success: bool
    message: str

class ResendCustomerPaymentOtpResponse(TypedDict, total=False):
    code: str
    description: str
    data: ResendCustomerPaymentOtpData

class FetchCheckoutTransactionDetailsData(TypedDict, total=False):
    status: bool
    message: str
    order: dict[str, Any]

class FetchCheckoutTransactionDetailsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchCheckoutTransactionDetailsData

class FetchCheckoutFlashAccountNumberData(TypedDict, total=False):
    accountNumber: str
    accountName: str
    bankName: str

class FetchCheckoutFlashAccountNumberResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchCheckoutFlashAccountNumberData

class RequestUserOtpToAuthenticateUserData(TypedDict, total=False):
    success: bool
    message: str

class RequestUserOtpToAuthenticateUserResponse(TypedDict, total=False):
    code: str
    description: str
    data: RequestUserOtpToAuthenticateUserData

class RequestUserOtpToAuthenticateUserWhoAlreadyHasSavedCardsData(TypedDict, total=False):
    success: bool
    message: str

class RequestUserOtpToAuthenticateUserWhoAlreadyHasSavedCardsResponse(TypedDict, total=False):
    code: str
    description: str
    data: RequestUserOtpToAuthenticateUserWhoAlreadyHasSavedCardsData

class SubmitUserOtpData(TypedDict, total=False):
    success: bool
    message: str

class SubmitUserOtpResponse(TypedDict, total=False):
    code: str
    description: str
    data: SubmitUserOtpData

class FetchUserSavedCardsData(TypedDict, total=False):
    tokenizedCardData: Any

class FetchUserSavedCardsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchUserSavedCardsData

class CancelCheckoutTransactionData(TypedDict, total=False):
    success: bool
    message: str

class CancelCheckoutTransactionResponse(TypedDict, total=False):
    code: str
    description: str
    data: CancelCheckoutTransactionData

class FetchBankCodesAndNamesData(TypedDict, total=False):
    results: list[dict[str, Any]]

class FetchBankCodesAndNamesResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchBankCodesAndNamesData

class PerformBankAccountLookupData(TypedDict, total=False):
    accountNumber: str
    accountName: str

class PerformBankAccountLookupResponse(TypedDict, total=False):
    code: str
    description: str
    data: PerformBankAccountLookupData

class PerformBankAccountTransferTheParentAccountData(TypedDict, total=False):
    amount: float
    meta: dict[str, Any]
    fee: float
    timeCreated: str
    id: str
    type: str
    status: str

class PerformBankAccountTransferTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: PerformBankAccountTransferTheParentAccountData

class PerformBankAccountTransferFromAccountData(TypedDict, total=False):
    amount: float
    meta: dict[str, Any]
    fee: float
    timeCreated: str
    id: str
    type: str
    status: str

class PerformBankAccountTransferFromAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: PerformBankAccountTransferFromAccountData

class PerformWalletTransferFromTheParentAccountData(TypedDict, total=False):
    amount: float
    meta: dict[str, Any]
    fee: float
    timeCreated: str
    id: str
    type: str
    status: str

class PerformWalletTransferFromTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: PerformWalletTransferFromTheParentAccountData

class PerformWalletTransferFromASubAccountData(TypedDict, total=False):
    amount: float
    meta: dict[str, Any]
    fee: float
    timeCreated: str
    id: str
    type: str
    status: str

class PerformWalletTransferFromASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: PerformWalletTransferFromASubAccountData

class AssignATerminalToAnAccountData(TypedDict, total=False):
    terminalId: str
    serialNumber: str
    accountId: str
    parentAccountId: str
    merchantName: str
    terminalLabel: str
    createdAt: str
    updatedAt: str

class AssignATerminalToAnAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: AssignATerminalToAnAccountData

class AssignATerminalToTheParentAccountData(TypedDict, total=False):
    terminalId: str
    serialNumber: str
    accountId: str
    parentAccountId: str
    merchantName: str
    terminalLabel: str
    createdAt: str
    updatedAt: str

class AssignATerminalToTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: AssignATerminalToTheParentAccountData

class UnAssignTerminalFromAnAccountData(TypedDict, total=False):
    terminalId: str
    serialNumber: str
    accountId: str
    parentAccountId: str
    merchantName: str
    terminalLabel: str
    createdAt: str
    updatedAt: str

class UnAssignTerminalFromAnAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: UnAssignTerminalFromAnAccountData

class UnAssignATerminalFromTheParentAccountData(TypedDict, total=False):
    terminalId: str
    serialNumber: str
    accountId: str
    parentAccountId: str
    merchantName: str
    terminalLabel: str
    createdAt: str
    updatedAt: str

class UnAssignATerminalFromTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: UnAssignATerminalFromTheParentAccountData

class FetchCreditDebitTransactionsOnASubAccountData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FetchCreditDebitTransactionsOnASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchCreditDebitTransactionsOnASubAccountData

class FetchCreditDebitTransactionsOnTheParentAccountData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FetchCreditDebitTransactionsOnTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchCreditDebitTransactionsOnTheParentAccountData

class FetchTransactionsOnASubAccountData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FetchTransactionsOnASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchTransactionsOnASubAccountData

class FilterAccountTransactionsData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FilterAccountTransactionsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FilterAccountTransactionsData

class FetchTransactionsOnTheParentAccountData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FetchTransactionsOnTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchTransactionsOnTheParentAccountData

class FilterParentAccountTransactionsData(TypedDict, total=False):
    results: list[dict[str, Any]]
    cursor: str

class FilterParentAccountTransactionsResponse(TypedDict, total=False):
    code: str
    description: str
    data: FilterParentAccountTransactionsData

class FetchASingleTransactionOnASubAccountData(TypedDict, total=False):
    id: str
    status: str
    amount: float
    fixedCharge: float
    source: str
    type: str
    gatewayMessage: str
    customerBillerId: str
    timeCreated: str
    posTid: str
    terminalId: str
    providerTerminalId: str
    rrn: str
    posSerialNumber: str
    posTerminalLabel: str
    stan: str
    paymentVendorReference: str
    userId: str
    posRrn: str
    merchantTxRef: str

class FetchASingleTransactionOnASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchASingleTransactionOnASubAccountData

class FetchASingleTransactionOnTheParentAccountData(TypedDict, total=False):
    id: str
    status: str
    amount: float
    fixedCharge: float
    source: str
    type: str
    gatewayMessage: str
    customerBillerId: str
    timeCreated: str
    posTid: str
    terminalId: str
    providerTerminalId: str
    rrn: str
    posSerialNumber: str
    posTerminalLabel: str
    stan: str
    paymentVendorReference: str
    userId: str
    posRrn: str
    merchantTxRef: str

class FetchASingleTransactionOnTheParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchASingleTransactionOnTheParentAccountData

class ConfirmATransactionSStatusBySessionIdData(TypedDict, total=False):
    id: str
    status: str
    amount: float
    fixedCharge: float
    source: str
    type: str
    gatewayMessage: str
    customerBillerId: str
    timeCreated: str
    posTid: str
    terminalId: str
    providerTerminalId: str
    rrn: str
    posSerialNumber: str
    posTerminalLabel: str
    stan: str
    paymentVendorReference: str
    userId: str
    posRrn: str
    merchantTxRef: str

class ConfirmATransactionSStatusBySessionIdResponse(TypedDict, total=False):
    code: str
    description: str
    data: ConfirmATransactionSStatusBySessionIdData

class FetchDataPlansAvailableOnATelcoNetworkProviderData(TypedDict, total=False):
    amount: int
    plan: str

class FetchDataPlansAvailableOnATelcoNetworkProviderResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchDataPlansAvailableOnATelcoNetworkProviderData

class MakeAirtimePurchasesViaParentAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str

class MakeAirtimePurchasesViaParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: MakeAirtimePurchasesViaParentAccountData

class MakeAirtimePurchasesViaSpecificOrSubAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str

class MakeAirtimePurchasesViaSpecificOrSubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: MakeAirtimePurchasesViaSpecificOrSubAccountData

class VendDataBundlesViaParentAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str

class VendDataBundlesViaParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: VendDataBundlesViaParentAccountData

class VendDataBundlesViaSpecificOrSubAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str

class VendDataBundlesViaSpecificOrSubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: VendDataBundlesViaSpecificOrSubAccountData

class CabletvLookupResponse(TypedDict, total=False):
    code: str
    description: str
    data: dict[str, Any]

class CableTvSubscriptionViaParentAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str
    id: str
    fee: str

class CableTvSubscriptionViaParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: CableTvSubscriptionViaParentAccountData

class CableTvSubscriptionViaASubAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str
    id: str
    fee: str

class CableTvSubscriptionViaASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: CableTvSubscriptionViaASubAccountData

class FetchElectricityProvidersData(TypedDict, total=False):
    id: str
    name: str

class FetchElectricityProvidersResponse(TypedDict, total=False):
    code: str
    description: str
    data: FetchElectricityProvidersData

class ElectricityCustomerLookupResponse(TypedDict, total=False):
    code: str
    description: str
    data: dict[str, Any]

class VendElectricityViaParentAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str
    id: str
    fee: str

class VendElectricityViaParentAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: VendElectricityViaParentAccountData

class VendElectricityViaASubAccountData(TypedDict, total=False):
    amount: float
    timeCreated: str
    type: str
    meta: dict[str, Any]
    status: str
    id: str
    fee: str

class VendElectricityViaASubAccountResponse(TypedDict, total=False):
    code: str
    description: str
    data: VendElectricityViaASubAccountData
