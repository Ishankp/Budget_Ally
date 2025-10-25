from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class KycCheckAddressSummary(BaseModel):
    type: str
    """Field describing whether the associated address is being used for commercial or residential purposes.
    
    Note: This value will be `no_data` when Plaid does not have sufficient data to determine the address's use."""

    summary: str
    """An enum indicating the match type between data provided by user and data checked against an external data source.
    
    
    `match` indicates that the provided input data was a strong match against external data.
    
    `partial_match` indicates the data approximately matched against external data. For example, "Knope" vs. "Knope-Wyatt" for last name.
    
    `no_match` indicates that Plaid was able to perform a check against an external data source and it did not match the provided input data.
    
    `no_data` indicates that Plaid was unable to find external data to compare against the provided input data.
    
    `no_input` indicates that Plaid was unable to perform a check because no information was provided for this field by the end user."""

    po_box: str
    """Field describing whether the associated address is a post office box. Will be `yes` when a P.O. box is detected, `no` when Plaid confirmed the address is not a P.O. box, and `no_data` when Plaid was not able to determine if the address is a P.O. box."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "KycCheckAddressSummary":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "KycCheckAddressSummary":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
