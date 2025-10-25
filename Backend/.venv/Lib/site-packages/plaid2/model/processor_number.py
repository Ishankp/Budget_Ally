from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .numbers_ach import NumbersAch
from .numbers_bacs import NumbersBacs
from .numbers_eft import NumbersEft
from .numbers_international import NumbersInternational


class ProcessorNumber(BaseModel):
    international: Optional[NumbersInternational] = None
    """Identifying information for transferring money to or from an international bank account via wire transfer."""

    eft: Optional[NumbersEft] = None
    """Identifying information for transferring money to or from a Canadian bank account via EFT."""

    ach: Optional[NumbersAch] = None
    """Identifying information for transferring money to or from a US account via ACH or wire transfer."""

    bacs: Optional[NumbersBacs] = None
    """Identifying information for transferring money to or from a UK bank account via BACS."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ProcessorNumber":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "ProcessorNumber":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
