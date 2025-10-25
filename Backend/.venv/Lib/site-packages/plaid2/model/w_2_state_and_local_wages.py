from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class W2StateAndLocalWages(BaseModel):
    employer_state_id_number: Optional[str] = None
    """State identification number of the employer."""

    state: Optional[str] = None
    """State associated with the wage."""

    locality_name: Optional[str] = None
    """Name of the locality."""

    local_income_tax: Optional[str] = None
    """Income tax from the locality."""

    local_wages_tips: Optional[str] = None
    """Wages and tips from the locality."""

    state_wages_tips: Optional[str] = None
    """Wages and tips from the specified state."""

    state_income_tax: Optional[str] = None
    """Income tax from the specified state."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "W2StateAndLocalWages":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "W2StateAndLocalWages":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
