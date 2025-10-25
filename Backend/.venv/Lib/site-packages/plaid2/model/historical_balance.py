from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class HistoricalBalance(BaseModel):
    current: float
    """The total amount of funds in the account, calculated from the `current` balance in the `balance` object by subtracting inflows and adding back outflows according to the posted date of each transaction.
    
    If the account has any pending transactions, historical balance amounts on or after the date of the earliest pending transaction may differ if retrieved in subsequent Asset Reports as a result of those pending transactions posting."""

    iso_currency_code: Optional[str] = None
    """The ISO-4217 currency code of the balance. Always `null` if `unofficial_currency_code` is non-`null`."""

    unofficial_currency_code: Optional[str] = None
    """The unofficial currency code associated with the balance. Always `null` if `iso_currency_code` is non-`null`.
    
    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s."""

    date: str
    """The date of the calculated historical balance, in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "HistoricalBalance":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "HistoricalBalance":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
