from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_1099 import Credit1099
from .credit_pay_stub import CreditPayStub
from .credit_w_2 import CreditW2


class PayrollIncomeObject(BaseModel):
    w_2_s: List[CreditW2]
    """Array of tax form W-2s."""

    form_1099_s: List[Credit1099]
    """Array of tax form 1099s."""

    pay_stubs: List[CreditPayStub]
    """Array of pay stubs for the user."""

    account_id: Optional[str] = None
    """ID of the payroll provider account."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PayrollIncomeObject":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PayrollIncomeObject":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
