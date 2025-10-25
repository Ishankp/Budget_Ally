from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .update_entity_screening_request_search_terms import UpdateEntityScreeningRequestSearchTerms


class UpdateEntityScreeningRequest(BaseModel):
    status: Optional[str] = None
    entity_watchlist_screening_id: str
    """ID of the associated entity screening."""

    assignee: Optional[str] = None
    search_terms: Optional[UpdateEntityScreeningRequestSearchTerms] = None
    """Search terms for editing an entity watchlist screening"""

    client_user_id: Optional[str] = None
    reset_fields: Optional[List[str]] = None
    """A list of fields to reset back to null"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "UpdateEntityScreeningRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "UpdateEntityScreeningRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
