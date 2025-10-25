from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .recipient_bacs import RecipientBacs


class ExternalPaymentInitiationConsentOptions(BaseModel):
    request_refund_details: Optional[bool] = None
    """When `true`, Plaid will attempt to request refund details from the payee's financial institution.  Support varies between financial institutions and will not always be available.  If refund details could be retrieved, they will be available in the `/payment_initiation/payment/get` response."""

    bacs: Optional[RecipientBacs] = None
    """An optional object used to restrict the accounts used for payments. If provided, the end user will be able to send payments only from the specified bank account."""

    iban: Optional[str] = None
    """The International Bank Account Number (IBAN) for the payer's account. If provided, the end user will be able to set up payment consent using only the specified bank account."""

    wallet_id: Optional[str] = None
    """The EMI (E-Money Institution) wallet that this payment consent is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ExternalPaymentInitiationConsentOptions":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "ExternalPaymentInitiationConsentOptions":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
