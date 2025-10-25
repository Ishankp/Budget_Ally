from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .pay import Pay


class EarningsTotal(BaseModel):
    hours: Optional[float] = None
    """Total number of hours worked for this pay period"""

    unofficial_currency_code: Optional[str] = None
    """The unofficial currency code associated with the security. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    
    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s."""

    ytd_amount: Optional[float] = None
    """The total year-to-date amount of the earnings"""

    iso_currency_code: Optional[str] = None
    """The ISO-4217 currency code of the line item. Always `null` if `unofficial_currency_code` is non-null."""

    current_pay: Optional[Pay] = None
    """An object representing a monetary amount."""

    current_amount: Optional[float] = None
    """Total amount of the earnings for this pay period"""

    ytd_pay: Optional[Pay] = None
    """An object representing a monetary amount."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "EarningsTotal":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "EarningsTotal":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
