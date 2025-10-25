from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class ProductAccess(BaseModel):
    accounts_statements: Optional[bool] = None
    """Allow access to "accounts_statements". Only used by certain partners. If relevant to the partner and unset, defaults to `true`."""

    accounts_tax_statements: Optional[bool] = None
    """Allow access to "accounts_tax_statements". Only used by certain partners. If relevant to the partner and unset, defaults to `true`."""

    customers_profiles: Optional[bool] = None
    """Allow access to "customers_profiles". Only used by certain partners. If relevant to the partner and unset, defaults to `true`."""

    auth: Optional[bool] = None
    """Allow access to account number details. Only used by certain partners. If relevant to the partner and unset, defaults to `true`."""

    transactions: Optional[bool] = None
    """Allow access to transaction details. Only used by certain partners. If relevant to the partner and unset, defaults to `true`."""

    identity: Optional[bool] = None
    """Allow access to the Identity product (name, email, phone, address). Only used by certain partners. If relevant to the partner and unset, defaults to `true`."""

    accounts_details_transactions: Optional[bool] = None
    """Allow access to "accounts_details_transactions". Only used by certain partners. If relevant to the partner and unset, defaults to `true`."""

    accounts_routing_number: Optional[bool] = None
    """Allow access to "accounts_routing_number". Only used by certain partners. If relevant to the partner and unset, defaults to `true`."""

    statements: Optional[bool] = None
    """Allow access to statements. Only used by certain partners. If relevant to the partner and unset, defaults to `true`."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ProductAccess":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "ProductAccess":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
