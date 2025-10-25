from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .generic_screening_hit_location_items import GenericScreeningHitLocationItems
from .screening_hit_date_of_birth_item import ScreeningHitDateOfBirthItem
from .screening_hit_documents_items import ScreeningHitDocumentsItems
from .screening_hit_names_items import ScreeningHitNamesItems


class ScreeningHitData(BaseModel):
    dates_of_birth: Optional[List[ScreeningHitDateOfBirthItem]] = None
    """Dates of birth associated with the watchlist hit"""

    names: Optional[List[ScreeningHitNamesItems]] = None
    """Names associated with the watchlist hit"""

    documents: Optional[List[ScreeningHitDocumentsItems]] = None
    """Documents associated with the watchlist hit"""

    locations: Optional[List[GenericScreeningHitLocationItems]] = None
    """Locations associated with the watchlist hit"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ScreeningHitData":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "ScreeningHitData":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
