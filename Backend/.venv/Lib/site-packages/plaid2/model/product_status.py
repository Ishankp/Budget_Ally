from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .product_status_breakdown import ProductStatusBreakdown


class ProductStatus(BaseModel):
    last_status_change: str
    """[ISO 8601](https://wikipedia.org/wiki/ISO_8601) formatted timestamp of the last status change for the institution.
    """

    status: str
    """This field is deprecated in favor of the `breakdown` object, which provides more granular institution health data.
    
    `HEALTHY`: the majority of requests are successful
    `DEGRADED`: only some requests are successful
    `DOWN`: all requests are failing"""

    breakdown: ProductStatusBreakdown
    """A detailed breakdown of the institution's performance for a request type. The values for `success`, `error_plaid`, and `error_institution` sum to 1."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ProductStatus":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "ProductStatus":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
