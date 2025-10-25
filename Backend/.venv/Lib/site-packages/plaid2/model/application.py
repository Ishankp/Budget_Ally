from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field

_ALIAS_MAP = {"name_": "name"}


class Application(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    country_code: Optional[str] = None
    """A string representing the country code of the client’s headquarters."""

    join_date: str
    """The date this application was granted production access at Plaid in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC."""

    name_: str
    """The name of the application"""

    application_id: str
    """This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect."""

    logo_url: Optional[str] = None
    """A URL that links to the application logo image."""

    company_legal_name: Optional[str] = None
    """A string representing the name of client’s legal entity."""

    city: Optional[str] = None
    """A string representing the city of the client’s headquarters."""

    region: Optional[str] = None
    """A string representing the region of the client’s headquarters."""

    reason_for_access: Optional[str] = None
    """A string provided by the connected app stating why they use their respective enabled products."""

    postal_code: Optional[str] = None
    """A string representing the postal code of the client’s headquarters."""

    display_name: Optional[str] = None
    """A human-readable name of the application for display purposes"""

    application_url: Optional[str] = None
    """The URL for the application's website"""

    use_case: Optional[str] = None
    """A string representing client’s broad use case as assessed by Plaid."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Application":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Application":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
