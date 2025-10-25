from typing import Any, Dict, Optional, Union
from pydantic import BaseModel


class PayrollItemStatus(BaseModel):
    processing_status: Optional[str] = None
    """Denotes the processing status for the verification.
    
    `UNKNOWN`: The processing status could not be determined.
    
    `PROCESSING_COMPLETE`: The processing has completed and the user has approved for sharing. The data is available to be retrieved.
    
    `PROCESSING`: The verification is still processing. The data is not available yet.
    
    `FAILED`: The processing failed to complete successfully.
    
    `APPROVAL_STATUS_PENDING`: The processing has completed but the user has not yet approved the sharing of the data."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PayrollItemStatus":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PayrollItemStatus":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
