from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class LinkTokenCreateRequestUserStatedIncomeSource(BaseModel):
    employer: Optional[str] = None
    """The employer corresponding to an income source specified by the user"""

    pay_per_cycle: Optional[float] = None
    """The income amount paid per cycle for a specified income source"""

    category: Optional[str] = None
    """The income category for a specified income source"""

    pay_frequency: Optional[str] = None
    """The pay frequency of a specified income source"""

    pay_annual: Optional[float] = None
    """The income amount paid annually for a specified income source"""

    pay_type: Optional[str] = None
    """The pay type - `GROSS`, `NET`, or `UNKNOWN` for a specified income source"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LinkTokenCreateRequestUserStatedIncomeSource":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "LinkTokenCreateRequestUserStatedIncomeSource":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
