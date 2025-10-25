from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PhysicalDocumentImages(BaseModel):
    original_back: Optional[str] = None
    """Temporary URL that expires after 60 seconds for downloading the original image of the back of the document. Might be null if the back of the document was not collected."""

    original_front: str
    """Temporary URL that expires after 60 seconds for downloading the uncropped original image of the front of the document."""

    cropped_back: Optional[str] = None
    """Temporary URL that expires after 60 seconds for downloading a cropped image containing just the back of the document. Might be null if the back of the document was not collected."""

    face: Optional[str] = None
    """Temporary URL that expires after 60 seconds for downloading a crop of just the user's face from the document image. Might be null if the document does not contain a face photo."""

    cropped_front: Optional[str] = None
    """Temporary URL that expires after 60 seconds for downloading a cropped image containing just the front of the document."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PhysicalDocumentImages":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PhysicalDocumentImages":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
