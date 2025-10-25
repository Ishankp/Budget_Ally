from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_bank_income_historical_summary import CreditBankIncomeHistoricalSummary


class CreditBankIncomeSummary(BaseModel):
    income_sources_count: Optional[int] = None
    """Number of income sources per end user."""

    unofficial_currency_code: Optional[str] = None
    """The unofficial currency code associated with the amount or balance. Always `null` if `iso_currency_code` is non-null.
    Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries."""

    start_date: Optional[str] = None
    """The earliest date within the days requested in which all income sources identified by Plaid appear in a user's account.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    end_date: Optional[str] = None
    """The latest date in which all income sources identified by Plaid appear in the user's account.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    income_categories_count: Optional[int] = None
    """Number of income categories per end user."""

    total_amount: Optional[float] = None
    """Total amount of earnings across all the income sources in the end user's Items for the days requested by the client."""

    income_transactions_count: Optional[int] = None
    """Number of income transactions per end user."""

    historical_summary: Optional[List[CreditBankIncomeHistoricalSummary]] = None
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
    def parse_obj(cls, data: Any) -> "CreditBankIncomeSummary":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditBankIncomeSummary":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
