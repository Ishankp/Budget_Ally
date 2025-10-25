from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .institutions_search_payment_initiation_options import InstitutionsSearchPaymentInitiationOptions


class InstitutionsSearchRequestOptions(BaseModel):
    include_optional_metadata: Optional[bool] = None
    """When true, return the institution's homepage URL, logo and primary brand color."""

    oauth: Optional[bool] = None
    """Limit results to institutions with or without OAuth login flows."""

    include_payment_initiation_metadata: Optional[bool] = None
    """When `true`, returns metadata related to the Payment Initiation product indicating which payment configurations are supported."""

    payment_initiation: Optional[InstitutionsSearchPaymentInitiationOptions] = None
    """Additional options that will be used to filter institutions by various Payment Initiation configurations."""

    include_auth_metadata: Optional[bool] = None
    """When `true`, returns metadata related to the Auth product indicating which auth methods are supported."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "InstitutionsSearchRequestOptions":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "InstitutionsSearchRequestOptions":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
