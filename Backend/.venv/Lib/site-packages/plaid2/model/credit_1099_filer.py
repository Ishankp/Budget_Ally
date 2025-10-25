from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_pay_stub_address import CreditPayStubAddress

_ALIAS_MAP = {"name_": "name"}


class Credit1099Filer(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    address: Optional[CreditPayStubAddress] = None
    """Address on the pay stub."""

    name_: Optional[str] = None
    """Name of filer."""

    type: Optional[str] = None
    """One of the following values will be provided: Payment Settlement Entity (PSE), Electronic Payment Fecilitator (EPF), Other Third Party"""

    tin: Optional[str] = None
    """Tax identification number of filer."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Credit1099Filer":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Credit1099Filer":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
