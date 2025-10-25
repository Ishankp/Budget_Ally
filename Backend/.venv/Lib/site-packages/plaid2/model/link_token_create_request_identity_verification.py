from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class LinkTokenCreateRequestIdentityVerification(BaseModel):
    consent: Optional[bool] = None
    template_id: str
    """ID of the associated Identity Verification template."""

    gave_consent: Optional[bool] = None
    """A flag specifying whether the end user has already agreed to a privacy policy specifying that their data will be shared with Plaid for verification purposes.
    
    If `gave_consent` is set to `true`, the `accept_tos` step will be marked as `skipped` and the end user's session will start at the next step requirement."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LinkTokenCreateRequestIdentityVerification":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "LinkTokenCreateRequestIdentityVerification":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
