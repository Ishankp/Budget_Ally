from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .distribution_breakdown import DistributionBreakdown


class PayPeriodDetails(BaseModel):
    start_date: Optional[str] = None
    """The pay period start date, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format: "yyyy-mm-dd"."""

    distribution_breakdown: Optional[List[DistributionBreakdown]] = None
    end_date: Optional[str] = None
    """The pay period end date, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format: "yyyy-mm-dd"."""

    gross_earnings: Optional[float] = None
    """Total earnings before tax/deductions."""

    pay_date: Optional[str] = None
    """The date on which the paystub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ("yyyy-mm-dd")."""

    pay_frequency: Optional[str] = None
    """The frequency at which an individual is paid."""

    pay_day: Optional[str] = None
    """The date on which the paystub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ("yyyy-mm-dd")."""

    check_amount: Optional[float] = None
    """The amount of the paycheck."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PayPeriodDetails":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PayPeriodDetails":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
