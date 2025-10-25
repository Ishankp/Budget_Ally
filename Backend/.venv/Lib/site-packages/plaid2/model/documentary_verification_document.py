from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .document_analysis import DocumentAnalysis
from .physical_document_extracted_data import PhysicalDocumentExtractedData
from .physical_document_images import PhysicalDocumentImages


class DocumentaryVerificationDocument(BaseModel):
    analysis: DocumentAnalysis
    """High level descriptions of how the associated document was processed. If a document fails verification, the details in the `analysis` object should help clarify why the document was rejected."""

    attempt: float
    """The `attempt` field begins with 1 and increments with each subsequent document upload."""

    status: str
    """An outcome status for this specific document submission. Distinct from the overall `documentary_verification.status` that summarizes the verification outcome from one or more documents."""

    images: PhysicalDocumentImages
    """URLs for downloading original and cropped images for this document submission. The URLs are designed to only allow downloading, not hot linking, so the URL will only serve the document image for 60 seconds before expiring. The expiration time is 60 seconds after the `GET` request for the associated Identity Verification attempt. A new expiring URL is generated with each request, so you can always rerequest the Identity Verification attempt if one of your URLs expires."""

    extracted_data: Optional[PhysicalDocumentExtractedData] = None
    """Data extracted from a user-submitted document."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "DocumentaryVerificationDocument":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "DocumentaryVerificationDocument":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
