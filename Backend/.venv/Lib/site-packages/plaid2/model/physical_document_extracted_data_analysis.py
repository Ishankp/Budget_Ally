from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field

_ALIAS_MAP = {"name_": "name"}


class PhysicalDocumentExtractedDataAnalysis(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    date_of_birth: str
    """A match summary describing the cross comparison between the subject's date of birth, extracted from the document image, and the date of birth they separately provided to the identity verification attempt."""

    expiration_date: str
    """A description of whether the associated document was expired when the verification was performed.
    
    Note: In the case where an expiration date is not present on the document or failed to be extracted, this value will be `no_data`."""

    issuing_country: str
    """A binary match indicator specifying whether the country that issued the provided document matches the country that the user separately provided to Plaid.
    
    Note: You can configure whether a `no_match` on `issuing_country` fails the `documentary_verification` by editing your Plaid Template."""

    name_: str
    """A match summary describing the cross comparison between the subject's name, extracted from the document image, and the name they separately provided to identity verification attempt."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PhysicalDocumentExtractedDataAnalysis":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PhysicalDocumentExtractedDataAnalysis":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
