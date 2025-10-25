from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .kyc_check_address_summary import KycCheckAddressSummary

_ALIAS_MAP = {"name_": "name"}


class KycCheckDetails(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    id_number: str
    """Result summary object specifying how the `id_number` field matched."""

    address: KycCheckAddressSummary
    """Result summary object specifying how the `address` field matched."""

    date_of_birth: str
    """Result summary object specifying how the `date_of_birth` field matched."""

    phone_number: str
    """Result summary object specifying how the `phone` field matched."""

    name_: str
    """Result summary object specifying how the `name` field matched."""

    status: str
    """The outcome status for the associated Identity Verification attempt's `kyc_check` step. This field will always have the same value as `steps.kyc_check`."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "KycCheckDetails":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "KycCheckDetails":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
