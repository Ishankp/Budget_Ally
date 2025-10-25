from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .physical_document_extracted_data_analysis import PhysicalDocumentExtractedDataAnalysis


class DocumentAnalysis(BaseModel):
    authenticity: str
    """High level summary of whether the document in the provided image matches the formatting rules and security checks for the associated jurisdiction.
    
    For example, most identity documents have formatting rules like the following:
    
    
    The image of the person's face must have a certain contrast in order to highlight skin tone
    
    
    The subject in the document's image must remove eye glasses and pose in a certain way
    
    
    The informational fields (name, date of birth, ID number, etc.) must be colored and aligned according to specific rules
    
    
    Security features like watermarks and background patterns must be present
    
    So a `match` status for this field indicates that the document in the provided image seems to conform to the various formatting and security rules associated with the detected document."""

    image_quality: str
    """A high level description of the quality of the image the user submitted.
    
    For example, an image that is blurry, distorted by glare from a nearby light source, or improperly framed might be marked as low or medium quality. Poor quality images are more likely to fail OCR and/or template conformity checks.
    
    Note: By default, Plaid will let a user recapture document images twice before failing the entire session if we attribute the failure to low image quality."""

    extracted_data: Optional[PhysicalDocumentExtractedDataAnalysis] = None
    """Analysis of the data extracted from the submitted document."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "DocumentAnalysis":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "DocumentAnalysis":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
