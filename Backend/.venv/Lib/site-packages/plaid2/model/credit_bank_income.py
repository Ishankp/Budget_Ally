from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_bank_income_item import CreditBankIncomeItem
from .credit_bank_income_summary import CreditBankIncomeSummary
from .credit_bank_income_warning import CreditBankIncomeWarning


class CreditBankIncome(BaseModel):
    items: Optional[List[CreditBankIncomeItem]] = None
    """The list of Items in the report along with the associated metadata about the Item."""

    bank_income_id: Optional[str] = None
    """The unique identifier associated with the Bank Income Report."""

    days_requested: Optional[int] = None
    """The number of days requested by the customer for the Bank Income Report."""

    generated_time: Optional[str] = None
    """The time when the Bank Income Report was generated."""

    bank_income_summary: Optional[CreditBankIncomeSummary] = None
    """Summary for bank income across all income sources and items (max history of 730 days)."""

    warnings: Optional[List[CreditBankIncomeWarning]] = None
    """If data from the Bank Income report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditBankIncome":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditBankIncome":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
