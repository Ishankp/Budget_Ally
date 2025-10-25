from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class Numbers(BaseModel):
    eft_institution: Optional[str] = None
    """EFT institution number. Must be specified alongside `eft_branch`."""

    account: Optional[str] = None
    """Will be used for the account number."""

    international_iban: Optional[str] = None
    """International bank account number (IBAN). If no account number is specified via `account`, will also be used as the account number by default. Must be specified alongside `international_bic`."""

    ach_wire_routing: Optional[str] = None
    """Must be a valid wire transfer routing number."""

    bacs_sort_code: Optional[str] = None
    """BACS sort code"""

    international_bic: Optional[str] = None
    """Bank identifier code (BIC). Must be specified alongside `international_iban`."""

    ach_routing: Optional[str] = None
    """Must be a valid ACH routing number."""

    eft_branch: Optional[str] = None
    """EFT branch number. Must be specified alongside `eft_institution`."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Numbers":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Numbers":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
