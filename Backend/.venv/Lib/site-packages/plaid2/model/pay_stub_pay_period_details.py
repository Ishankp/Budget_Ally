from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .pay_stub_distribution_breakdown import PayStubDistributionBreakdown


class PayStubPayPeriodDetails(BaseModel):
    iso_currency_code: Optional[str] = None
    """The ISO-4217 currency code of the net pay. Always `null` if `unofficial_currency_code` is non-null."""

    distribution_breakdown: List[PayStubDistributionBreakdown]
    pay_date: Optional[str] = None
    """The date on which the pay stub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ("yyyy-mm-dd")."""

    end_date: Optional[str] = None
    """The date on which the pay period ended, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ("yyyy-mm-dd")."""

    pay_amount: Optional[float] = None
    """The amount of the paycheck."""

    gross_earnings: Optional[float] = None
    """Total earnings before tax/deductions."""

    unofficial_currency_code: Optional[str] = None
    """The unofficial currency code associated with the net pay. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    
    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s."""

    pay_frequency: Optional[str] = None
    """The frequency at which an individual is paid."""

    start_date: Optional[str] = None
    """The date on which the pay period started, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ("yyyy-mm-dd")."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PayStubPayPeriodDetails":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PayStubPayPeriodDetails":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
