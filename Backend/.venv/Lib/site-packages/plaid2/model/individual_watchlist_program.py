from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .watchlist_screening_audit_trail import WatchlistScreeningAuditTrail

_ALIAS_MAP = {"name_": "name"}


class IndividualWatchlistProgram(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    id: str
    """ID of the associated program."""

    is_rescanning_enabled: bool
    """Indicator specifying whether the program is enabled and will perform daily rescans."""

    lists_enabled: List[str]
    """Watchlists enabled for the associated program"""

    name_sensitivity: str
    """The valid name matching sensitivity configurations for a screening program. Note that while certain matching techniques may be more prevalent on less strict settings, all matching algorithms are enabled for every sensitivity.
    
    `coarse` - See more potential matches. This sensitivity will see more broad phonetic matches across alphabets that make missing a potential hit very unlikely. This setting is noisier and will require more manual review.
    
    `balanced` - A good default for most companies. This sensitivity is balanced to show high quality hits with reduced noise.
    
    `strict` - Aggressive false positive reduction. This sensitivity will require names to be more similar than `coarse` and `balanced` settings, relying less on phonetics, while still accounting for character transpositions, missing tokens, and other common permutations.
    
    `exact` - Matches must be nearly exact. This sensitivity will only show hits with exact or nearly exact name matches with only basic correction such as extraneous symbols and capitalization. This setting is generally not recommended unless you have a very specific use case."""

    created_at: str
    """An ISO8601 formatted timestamp."""

    name_: str
    """A name for the program to define its purpose. For example, "High Risk Individuals", "US Cardholders", or "Applicants"."""

    is_archived: bool
    """Archived programs are read-only and cannot screen new customers nor participate in ongoing monitoring."""

    audit_trail: WatchlistScreeningAuditTrail
    """Information about the last change made to the parent object specifying what caused the change as well as when it occurred."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IndividualWatchlistProgram":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IndividualWatchlistProgram":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
