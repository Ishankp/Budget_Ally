from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .asset_report_user import AssetReportUser


class AssetReportCreateRequestOptions(BaseModel):
    webhook: Optional[str] = None
    """URL to which Plaid will send Assets webhooks, for example when the requested Asset Report is ready."""

    products: Optional[List[str]] = None
    """Additional information that can be included in the asset report. Possible values: `"investments"`"""

    user: Optional[AssetReportUser] = None
    """The user object allows you to provide additional information about the user to be appended to the Asset Report. All fields are optional. The `first_name`, `last_name`, and `ssn` fields are required if you would like the Report to be eligible for Fannie Mae’s Day 1 Certainty™ program."""

    client_report_id: Optional[str] = None
    """Client-generated identifier, which can be used by lenders to track loan applications."""

    include_fast_report: Optional[bool] = None
    """true to return balance and identity earlier as a fast report. Defaults to false if omitted."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "AssetReportCreateRequestOptions":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "AssetReportCreateRequestOptions":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
