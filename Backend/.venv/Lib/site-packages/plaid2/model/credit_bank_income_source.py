from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_bank_income_historical_summary import CreditBankIncomeHistoricalSummary


class CreditBankIncomeSource(BaseModel):
    total_amount: Optional[float] = None
    """Total amount of earnings in the user’s bank account for the specific income source for days requested by the client."""

    income_category: Optional[str] = None
    """The income category."""

    start_date: Optional[str] = None
    """Minimum of all dates within the specific income sources in the user's bank account for days requested by the client.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    end_date: Optional[str] = None
    """Maximum of all dates within the specific income sources in the user’s bank account for days requested by the client.
    The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    income_source_id: Optional[str] = None
    """A unique identifier for an income source."""

    historical_summary: Optional[List[CreditBankIncomeHistoricalSummary]] = None
    transaction_count: Optional[int] = None
    """Number of transactions for the income source within the start and end date."""

    pay_frequency: Optional[str] = None
    """The income pay frequency."""

    account_id: Optional[str] = None
    """Plaid's unique idenfier for the account."""

    income_description: Optional[str] = None
    """The most common name or original description for the underlying income transactions."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditBankIncomeSource":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditBankIncomeSource":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
