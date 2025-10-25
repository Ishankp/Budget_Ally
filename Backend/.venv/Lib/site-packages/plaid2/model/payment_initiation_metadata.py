from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .payment_initiation_maximum_payment_amount import PaymentInitiationMaximumPaymentAmount
from .payment_initiation_standing_order_metadata import PaymentInitiationStandingOrderMetadata


class PaymentInitiationMetadata(BaseModel):
    maximum_payment_amount: PaymentInitiationMaximumPaymentAmount
    """A mapping of currency to maximum payment amount (denominated in the smallest unit of currency) supported by the institution.
    
    Example: `{"GBP": "10000"}`
    """

    supports_refund_details: bool
    """Indicates whether the institution supports returning refund details when initiating a payment."""

    supports_international_payments: bool
    """Indicates whether the institution supports payments from a different country."""

    supports_sepa_instant: bool
    """Indicates whether the institution supports SEPA Instant payments."""

    standing_order_metadata: Optional[PaymentInitiationStandingOrderMetadata] = None
    """Metadata specifically related to valid Payment Initiation standing order configurations for the institution."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentInitiationMetadata":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PaymentInitiationMetadata":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
