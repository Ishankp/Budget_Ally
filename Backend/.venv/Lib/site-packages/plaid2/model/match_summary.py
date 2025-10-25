from typing import Any, Dict, Union
from pydantic import BaseModel


class MatchSummary(BaseModel):
    summary: str
    """An enum indicating the match type between data provided by user and data checked against an external data source.
    
    
    `match` indicates that the provided input data was a strong match against external data.
    
    `partial_match` indicates the data approximately matched against external data. For example, "Knope" vs. "Knope-Wyatt" for last name.
    
    `no_match` indicates that Plaid was able to perform a check against an external data source and it did not match the provided input data.
    
    `no_data` indicates that Plaid was unable to find external data to compare against the provided input data.
    
    `no_input` indicates that Plaid was unable to perform a check because no information was provided for this field by the end user."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "MatchSummary":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "MatchSummary":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
