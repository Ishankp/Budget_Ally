from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class InflowModel(BaseModel):
    statement_day_of_month: str
    """Number between 1 and 28, or `last` meaning the last day of the month. The day of the month on which the balance is calculated for the next payment. The name of the income transaction. This field is required if `type` is `monthly-balance-payment` or `monthly-interest-only-payment`."""

    transaction_name: str
    """The name of the income transaction. This field is required if `type` is `monthly-income`, `monthly-balance-payment` or `monthly-interest-only-payment`."""

    income_amount: float
    """Amount of income per month. This value is required if `type` is `monthly-income`."""

    type: str
    """Inflow model. One of the following:
    
    `none`: No income
    
    `monthly-income`: Income occurs once per month `monthly-balance-payment`: Pays off the balance on a liability account at the given statement day of month.
    
    `monthly-interest-only-payment`: Makes an interest-only payment on a liability account at the given statement day of month.
    
    Note that account types supported by Liabilities will accrue interest in the Sandbox. The types impacted are account type `credit` with subtype `credit` or `paypal`, and account type `loan` with subtype `student` or `mortgage`."""

    payment_day_of_month: float
    """Number between 1 and 28, or `last` meaning the last day of the month. The day of the month on which the income transaction will appear. The name of the income transaction. This field is required if `type` is `monthly-income`, `monthly-balance-payment` or `monthly-interest-only-payment`."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "InflowModel":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "InflowModel":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
