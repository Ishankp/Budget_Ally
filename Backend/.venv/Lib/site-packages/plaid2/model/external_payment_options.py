from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .recipient_bacs import RecipientBacs


class ExternalPaymentOptions(BaseModel):
    request_refund_details: Optional[bool] = None
    """When `true`, Plaid will attempt to request refund details from the payee's financial institution.  Support varies between financial institutions and will not always be available.  If refund details could be retrieved, they will be available in the `/payment_initiation/payment/get` response."""

    wallet_id: Optional[str] = None
    """The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests."""

    bacs: Optional[RecipientBacs] = None
    """An optional object used to restrict the accounts used for payments. If provided, the end user will be able to send payments only from the specified bank account."""

    scheme: Optional[str] = None
    """Payment scheme. If not specified - the default in the region will be used (e.g. `SEPA_CREDIT_TRANSFER` for EU). Using unsupported values will result in a failed payment.
    
    `FASTER_PAYMENTS`: Enables payments to move quickly between UK bank accounts. Default value in the UK.
    
    `SEPA_CREDIT_TRANSFER`: The standard payment to a beneficiary within the SEPA area.
    
    `SEPA_CREDIT_TRANSFER_INSTANT`: Instant payment within the SEPA area. May involve additional fees and may not be available at some banks."""

    iban: Optional[str] = None
    """The International Bank Account Number (IBAN) for the payer's account. If provided, the end user will be able to send payments only from the specified bank account."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ExternalPaymentOptions":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "ExternalPaymentOptions":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
