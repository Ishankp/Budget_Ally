from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class IncomeBreakdown(BaseModel):
    type: Optional[str] = None
    """The type of income. Possible values include:
      `"regular"`: regular income
      `"overtime"`: overtime income
      `"bonus"`: bonus income"""

    hours: Optional[float] = None
    """The number of hours logged for this income for this pay period."""

    rate: Optional[float] = None
    """The hourly rate at which the income is paid."""

    total: Optional[float] = None
    """The total pay for this pay period."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IncomeBreakdown":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IncomeBreakdown":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
