from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class AssetsRelayWebhook(BaseModel):
    asset_relay_token: str
    """The `asset_relay_token` that was created by calling `/asset_report/relay/create."""

    relay_event: str
    """The webhook code indicating which endpoint was called. It can be one of `GET_CALLED`, `REFRESH_CALLED` or `AUDIT_COPY_CREATE_CALLED`."""

    secondary_client_id: str
    """The id of the client with whom the Asset Report is being shared."""

    webhook_type: str
    """`ASSETS`"""

    webhook_code: str
    """`RELAY_EVENT`"""

    asset_report_id: str
    """The `asset_report_id` that can be provided to `/asset_report/relay/get` to retrieve the Asset Report."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "AssetsRelayWebhook":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "AssetsRelayWebhook":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
