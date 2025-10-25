from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .pay import Pay


class DistributionBreakdown(BaseModel):
    unofficial_currency_code: Optional[str] = None
    """The unofficial currency code associated with the net pay. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    
    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s."""

    type: Optional[str] = None
    """Type of the account that the paystub was sent to (e.g. 'checking')."""

    current_pay: Optional[Pay] = None
    """An object representing a monetary amount."""

    bank_name: Optional[str] = None
    """The name of the bank that the payment is being deposited to."""

    iso_currency_code: Optional[str] = None
    """The ISO-4217 currency code of the net pay. Always `null` if `unofficial_currency_code` is non-null."""

    current_amount: Optional[float] = None
    """The amount distributed to this account."""

    account_name: Optional[str] = None
    """Name of the account for the given distribution."""

    mask: Optional[str] = None
    """The last 2-4 alphanumeric characters of an account's official account number."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "DistributionBreakdown":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "DistributionBreakdown":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
