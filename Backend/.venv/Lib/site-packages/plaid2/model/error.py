from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class Error(BaseModel):
    status: Optional[float] = None
    """The HTTP status code associated with the error. This will only be returned in the response body when the error information is provided via a webhook."""

    causes: Optional[List[Any]] = None
    """In the Assets product, a request can pertain to more than one Item. If an error is returned for such a request, `causes` will return an array of errors containing a breakdown of these errors on the individual Item level, if any can be identified.
    
    `causes` will only be provided for the `error_type` `ASSET_REPORT_ERROR`. `causes` will also not be populated inside an error nested within a `warning` object."""

    display_message: Optional[str] = None
    """A user-friendly representation of the error code. `null` if the error is not related to user action.
    
    This may change over time and is not safe for programmatic use."""

    error_type: str
    """A broad categorization of the error. Safe for programmatic use."""

    request_id: Optional[str] = None
    """A unique ID identifying the request, to be used for troubleshooting purposes. This field will be omitted in errors provided by webhooks."""

    documentation_url: Optional[str] = None
    """The URL of a Plaid documentation page with more information about the error"""

    error_code: str
    """The particular error code. Safe for programmatic use."""

    error_message: str
    """A developer-friendly representation of the error code. This may change over time and is not safe for programmatic use."""

    suggested_action: Optional[str] = None
    """Suggested steps for resolving the error"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Error":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Error":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
