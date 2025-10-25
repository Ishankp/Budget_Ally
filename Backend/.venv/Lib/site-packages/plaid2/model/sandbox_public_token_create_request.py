from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .sandbox_public_token_create_request_options import SandboxPublicTokenCreateRequestOptions


class SandboxPublicTokenCreateRequest(BaseModel):
    options: Optional[SandboxPublicTokenCreateRequestOptions] = None
    """An optional set of options to be used when configuring the Item. If specified, must not be `null`."""

    user_token: Optional[str] = None
    """The user token associated with the User data is being requested for."""

    institution_id: str
    """The ID of the institution the Item will be associated with"""

    initial_products: List[str]
    """The products to initially pull for the Item. May be any products that the specified `institution_id`  supports. This array may not be empty."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "SandboxPublicTokenCreateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "SandboxPublicTokenCreateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
