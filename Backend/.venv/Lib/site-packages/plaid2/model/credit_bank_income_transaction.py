from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field

_ALIAS_MAP = {"name_": "name"}


class CreditBankIncomeTransaction(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    unofficial_currency_code: Optional[str] = None
    """The unofficial currency code associated with the amount or balance. Always `null` if `iso_currency_code` is non-null.
    Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries."""

    name_: Optional[str] = None
    """The merchant name or transaction description."""

    amount: Optional[float] = None
    """The settled value of the transaction, denominated in the transactions's currency as stated in `iso_currency_code` or `unofficial_currency_code`.
    Positive values when money moves out of the account; negative values when money moves in.
    For example, credit card purchases are positive; credit card payment, direct deposits, and refunds are negative."""

    check_number: Optional[str] = None
    """The check number of the transaction. This field is only populated for check transactions."""

    iso_currency_code: Optional[str] = None
    """The ISO 4217 currency code of the amount or balance."""

    pending: Optional[bool] = None
    """When true, identifies the transaction as pending or unsettled.
    Pending transaction details (name, type, amount, category ID) may change before they are settled."""

    transaction_id: Optional[str] = None
    """The unique ID of the transaction. Like all Plaid identifiers, the `transaction_id` is case sensitive."""

    date: Optional[str] = None
    """For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted.
    Both dates are returned in an ISO 8601 format (YYYY-MM-DD)."""

    original_description: Optional[str] = None
    """The string returned by the financial institution to describe the transaction."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditBankIncomeTransaction":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditBankIncomeTransaction":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
