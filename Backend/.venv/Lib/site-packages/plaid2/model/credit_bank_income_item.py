from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_bank_income_account import CreditBankIncomeAccount
from .credit_bank_income_source import CreditBankIncomeSource


class CreditBankIncomeItem(BaseModel):
    item_id: Optional[str] = None
    """The unique identifier for the Item."""

    bank_income_accounts: Optional[List[CreditBankIncomeAccount]] = None
    """The Item's accounts that have Bank Income data."""

    bank_income_sources: Optional[List[CreditBankIncomeSource]] = None
    """The income sources for this Item. Each entry in the array is a single income source."""

    last_updated_time: Optional[str] = None
    """The time when this Item's data was last retrieved from the financial institution."""

    institution_id: Optional[str] = None
    """The unique identifier of the institution associated with the Item."""

    institution_name: Optional[str] = None
    """The name of the institution associated with the Item."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditBankIncomeItem":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditBankIncomeItem":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
