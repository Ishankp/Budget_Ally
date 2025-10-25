from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .watchlist_screening_audit_trail import WatchlistScreeningAuditTrail


class EntityWatchlistScreeningReview(BaseModel):
    audit_trail: WatchlistScreeningAuditTrail
    """Information about the last change made to the parent object specifying what caused the change as well as when it occurred."""

    id: str
    """ID of the associated entity review."""

    confirmed_hits: List[str]
    """Hits marked as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected."""

    dismissed_hits: List[str]
    """Hits marked as a false positive after thorough manual review. These hits will never recur or be updated once dismissed."""

    comment: Optional[str] = None
    """A comment submitted by a team member as part of reviewing a watchlist screening."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "EntityWatchlistScreeningReview":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "EntityWatchlistScreeningReview":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
