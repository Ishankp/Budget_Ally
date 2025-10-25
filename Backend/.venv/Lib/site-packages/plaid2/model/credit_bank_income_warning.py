from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_bank_income_cause import CreditBankIncomeCause


class CreditBankIncomeWarning(BaseModel):
    warning_code: Optional[str] = None
    """The warning code identifies a specific kind of warning.
    `IDENTITY_UNAVAILABLE`: Unable to extract identity for the Item
    `TRANSACTIONS_UNAVAILABLE`: Unable to extract transactions for the Item
    `ITEM_UNAPPROVED`: User did not grant permission to share income data for the Item
    `REPORT_DELETED`: Report deleted due to customer or consumer request"""

    warning_type: Optional[str] = None
    """The warning type which will always be `BANK_INCOME_WARNING`."""

    cause: Optional[CreditBankIncomeCause] = None
    """An error object and associated `item_id` used to identify a specific Item and error when a batch operation operating on multiple Items has encountered an error in one of the Items."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditBankIncomeWarning":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditBankIncomeWarning":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
