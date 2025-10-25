from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .update_individual_screening_request_search_terms import UpdateIndividualScreeningRequestSearchTerms


class UpdateIndividualScreeningRequest(BaseModel):
    watchlist_screening_id: str
    """ID of the associated screening."""

    search_terms: Optional[UpdateIndividualScreeningRequestSearchTerms] = None
    """Search terms for editing an individual watchlist screening"""

    assignee: Optional[str] = None
    status: Optional[str] = None
    reset_fields: Optional[List[str]] = None
    """A list of fields to reset back to null"""

    client_user_id: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "UpdateIndividualScreeningRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "UpdateIndividualScreeningRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
