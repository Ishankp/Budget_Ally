from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .account_filters_response import AccountFiltersResponse


class LinkTokenGetMetadataResponse(BaseModel):
    country_codes: List[str]
    """The `country_codes` specified in the `/link/token/create` call."""

    language: Optional[str] = None
    """The `language` specified in the `/link/token/create` call."""

    client_name: Optional[str] = None
    """The `client_name` specified in the `/link/token/create` call."""

    redirect_uri: Optional[str] = None
    """The `redirect_uri` specified in the `/link/token/create` call."""

    initial_products: List[str]
    """The `products` specified in the `/link/token/create` call."""

    institution_data: Optional[str] = None
    """A map containing data used to highlight institutions in Link."""

    webhook: Optional[str] = None
    """The `webhook` specified in the `/link/token/create` call."""

    account_filters: Optional[AccountFiltersResponse] = None
    """The `account_filters` specified in the original call to `/link/token/create`.
    """

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LinkTokenGetMetadataResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "LinkTokenGetMetadataResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
