from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_bank_income_transaction import CreditBankIncomeTransaction


class CreditBankIncomeHistoricalSummary(BaseModel):
    start_date: Optional[str] = None
    """The start date of the period covered in this monthly summary.
    This date will be the first day of the month, unless the month being covered is a partial month because it is the first month included in the summary and the date range being requested does not begin with the first day of the month.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    total_amount: Optional[float] = None
    """Total amount of earnings for the income source(s) of the user for the month in the summary."""

    unofficial_currency_code: Optional[str] = None
    """The unofficial currency code associated with the amount or balance. Always `null` if `iso_currency_code` is non-null.
    Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries."""

    end_date: Optional[str] = None
    """The end date of the period included in this monthly summary.
    This date will be the last day of the month, unless the month being covered is a partial month because it is the last month included in the summary and the date range being requested does not end with the last day of the month.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    transactions: Optional[List[CreditBankIncomeTransaction]] = None
    iso_currency_code: Optional[str] = None
    """The ISO 4217 currency code of the amount or balance."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditBankIncomeHistoricalSummary":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditBankIncomeHistoricalSummary":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
