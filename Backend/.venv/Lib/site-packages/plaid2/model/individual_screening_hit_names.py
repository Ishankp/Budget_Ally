from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class IndividualScreeningHitNames(BaseModel):
    is_primary: bool
    """Primary names are those most commonly used to refer to this person. Only one name will ever be marked as primary."""

    weak_alias_determination: str
    """Names that are explicitly marked as low quality either by their `source` list, or by `plaid` by a series of additional checks done by Plaid. Plaid does not ever surface a hit as a result of a weak name alone. If a name has no quality issues, this value will be `none`."""

    full: str
    """The full name of the individual, including all parts."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IndividualScreeningHitNames":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IndividualScreeningHitNames":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
