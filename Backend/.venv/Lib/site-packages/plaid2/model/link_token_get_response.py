from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .link_token_get_metadata_response import LinkTokenGetMetadataResponse


class LinkTokenGetResponse(BaseModel):
    created_at: Optional[str] = None
    """The creation timestamp for the `link_token`, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format."""

    metadata: LinkTokenGetMetadataResponse
    """An object specifying the arguments originally provided to the `/link/token/create` call."""

    expiration: Optional[str] = None
    """The expiration timestamp for the `link_token`, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format."""

    link_token: str
    """A `link_token`, which can be supplied to Link in order to initialize it and receive a `public_token`, which can be exchanged for an `access_token`."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LinkTokenGetResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "LinkTokenGetResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
