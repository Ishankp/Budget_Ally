from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_pay_stub_address import CreditPayStubAddress
from .pay_stub_taxpayer_id import PayStubTaxpayerId

_ALIAS_MAP = {"name_": "name"}


class CreditPayStubEmployee(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    address: CreditPayStubAddress
    """Address on the pay stub."""

    name_: Optional[str] = None
    """The name of the employee."""

    taxpayer_id: PayStubTaxpayerId
    """Taxpayer ID of the individual receiving the paystub."""

    marital_status: Optional[str] = None
    """Marital status of the employee - either `SINGLE` or `MARRIED`."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditPayStubEmployee":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditPayStubEmployee":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
