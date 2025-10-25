from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PaymentInitiationStandingOrderMetadata(BaseModel):
    supports_standing_order_end_date: bool
    """Indicates whether the institution supports closed-ended standing orders by providing an end date."""

    supports_standing_order_negative_execution_days: bool
    """This is only applicable to `MONTHLY` standing orders. Indicates whether the institution supports negative integers (-1 to -5) for setting up a `MONTHLY` standing order relative to the end of the month."""

    valid_standing_order_intervals: List[str]
    """A list of the valid standing order intervals supported by the institution."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentInitiationStandingOrderMetadata":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PaymentInitiationStandingOrderMetadata":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
