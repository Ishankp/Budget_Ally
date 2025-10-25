from typing import Any, Dict, Optional, Union
from pydantic import BaseModel


class LinkTokenCreateRequestUpdate(BaseModel):
    account_selection_enabled: Optional[bool] = None
    """If `true`, enables [update mode with Account Select](https://plaid.com/docs/link/update-mode/#using-update-
    mode-to-request-new-accounts)."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LinkTokenCreateRequestUpdate":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "LinkTokenCreateRequestUpdate":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
