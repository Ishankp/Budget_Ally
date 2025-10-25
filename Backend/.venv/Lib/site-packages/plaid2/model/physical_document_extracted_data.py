from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PhysicalDocumentExtractedData(BaseModel):
    expiration_date: Optional[str] = None
    category: str
    """The type of identity document detected in the images provided. Will always be one of the following values:
    
      `drivers_license` - A driver's license for the associated country
    
      `id_card` - A general national identification card, distinct from driver's licenses
    
      `passport` - A passport for the associated country
    
      `residence_permit_card` - An identity document permitting a foreign citizen to <em>temporarily</em> reside in the associated country
    
      `resident_card` - An identity document permitting a foreign citizen to <em>permanently</em> reside in the associated country
    
    Note: This value may be different from the ID type that the user selects within Link. For example, if they select "Driver's License" but then submit a picture of a passport, this field will say `passport`"""

    id_number: Optional[str] = None
    """Alpha-numeric ID number extracted via OCR from the user's document image."""

    issuing_country: str
    """Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2 form."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PhysicalDocumentExtractedData":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PhysicalDocumentExtractedData":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
