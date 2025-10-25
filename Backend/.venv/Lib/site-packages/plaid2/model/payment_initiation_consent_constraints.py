from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .payment_amount import PaymentAmount
from .payment_consent_periodic_amount import PaymentConsentPeriodicAmount
from .payment_consent_valid_date_time import PaymentConsentValidDateTime


class PaymentInitiationConsentConstraints(BaseModel):
    max_payment_amount: PaymentAmount
    """Maximum amount of a single payment initiated using the payment consent."""

    valid_date_time: Optional[PaymentConsentValidDateTime] = None
    """Life span for the payment consent. After the `to` date the payment consent expires and can no longer be used for payment initiation."""

    periodic_amounts: List[PaymentConsentPeriodicAmount]
    """A list of amount limitations per period of time."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentInitiationConsentConstraints":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PaymentInitiationConsentConstraints":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
