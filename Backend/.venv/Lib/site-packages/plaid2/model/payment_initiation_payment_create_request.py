from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .external_payment_options import ExternalPaymentOptions
from .external_payment_schedule_base import ExternalPaymentScheduleBase
from .payment_amount import PaymentAmount


class PaymentInitiationPaymentCreateRequest(BaseModel):
    amount: PaymentAmount
    """The amount and currency of a payment"""

    recipient_id: str
    """The ID of the recipient the payment is for."""

    reference: str
    """A reference for the payment. This must be an alphanumeric string with at most 18 characters and must not contain any special characters (since not all institutions support them)."""

    schedule: Optional[ExternalPaymentScheduleBase] = None
    """The schedule that the payment will be executed on. If a schedule is provided, the payment is automatically set up as a standing order. If no schedule is specified, the payment will be executed only once."""

    options: Optional[ExternalPaymentOptions] = None
    """Additional payment options"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentInitiationPaymentCreateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PaymentInitiationPaymentCreateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
