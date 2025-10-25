from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class LinkTokenCreateRequestAuth(BaseModel):
    flow_type: Optional[str] = None
    """This field has been deprecated in favor of `auth_type_select_enabled`."""

    auth_type_select_enabled: Optional[bool] = None
    """Specifies whether Auth Type Select is enabled for the Link session, allowing the end user to choose between linking instantly or manually prior to selecting their financial institution. Note that this can only be true if `same_day_microdeposits_enabled` is set to true."""

    automated_microdeposits_enabled: Optional[bool] = None
    """Specifies whether the Link session is enabled for the Automated Micro-deposits flow."""

    instant_match_enabled: Optional[bool] = None
    """Specifies whether the Link session is enabled for the Instant Match flow."""

    same_day_microdeposits_enabled: Optional[bool] = None
    """Specifies whether the Link session is enabled for the Same Day Micro-deposits flow."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LinkTokenCreateRequestAuth":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "LinkTokenCreateRequestAuth":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
