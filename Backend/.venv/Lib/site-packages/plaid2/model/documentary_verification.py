from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .documentary_verification_document import DocumentaryVerificationDocument


class DocumentaryVerification(BaseModel):
    status: str
    """The outcome status for the associated Identity Verification attempt's `documentary_verification` step. This field will always have the same value as `steps.documentary_verification`."""

    documents: List[DocumentaryVerificationDocument]
    """An array of documents submitted to the `documentary_verification` step. Each entry represents one user submission, where each submission will contain both a front and back image, or just a front image, depending on the document type.
    
    Note: Plaid will automatically let a user submit a new set of document images up to three times if we detect that a previous attempt might have failed due to user error. For example, if the first set of document images are blurry or obscured by glare, the user will be asked to capture their documents again, resulting in at least two separate entries within `documents`. If the overall `documentary_verification` is `failed`, the user has exhausted their retry attempts."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "DocumentaryVerification":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "DocumentaryVerification":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
