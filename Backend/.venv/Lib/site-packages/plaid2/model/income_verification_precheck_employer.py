from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .income_verification_precheck_employer_address import IncomeVerificationPrecheckEmployerAddress

_ALIAS_MAP = {"name_": "name"}


class IncomeVerificationPrecheckEmployer(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    address: Optional[IncomeVerificationPrecheckEmployerAddress] = None
    """The address of the employer"""

    tax_id: Optional[str] = None
    """The employer's tax id"""

    name_: Optional[str] = None
    """The employer's name"""

    url: Optional[str] = None
    """The URL for the employer's public website"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IncomeVerificationPrecheckEmployer":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IncomeVerificationPrecheckEmployer":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
