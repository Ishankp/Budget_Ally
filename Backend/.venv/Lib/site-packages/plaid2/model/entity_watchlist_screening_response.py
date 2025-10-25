from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .entity_watchlist_screening_search_terms import EntityWatchlistScreeningSearchTerms
from .watchlist_screening_audit_trail import WatchlistScreeningAuditTrail


class EntityWatchlistScreeningResponse(BaseModel):
    audit_trail: WatchlistScreeningAuditTrail
    """Information about the last change made to the parent object specifying what caused the change as well as when it occurred."""

    assignee: Optional[str] = None
    client_user_id: Optional[str] = None
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""

    id: str
    """ID of the associated entity screening."""

    status: str
    """A status enum indicating whether a screening is still pending review, has been rejected, or has been cleared."""

    search_terms: EntityWatchlistScreeningSearchTerms
    """Search terms associated with an entity used for searching against watchlists"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "EntityWatchlistScreeningResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "EntityWatchlistScreeningResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
