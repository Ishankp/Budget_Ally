from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field

_ALIAS_MAP = {"name_": "name"}


class CreditDocumentMetadata(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field: _ALIAS_MAP.get(field, field)

    name_: str
    """The name of the document."""

    document_type: Optional[str] = None
    """The type of document.
    
    `PAYSTUB`: A paystub.
    
    `BANK_STATEMENT`: A bank statement.
    
    `US_TAX_W2`: A W-2 wage and tax statement provided by a US employer reflecting wages earned by the employee.
    
    `US_MILITARY_ERAS`: An electronic Retirement Account Statement (eRAS) issued by the US military.
    
    `US_MILITARY_LES`: A Leave and Earnings Statement (LES) issued by the US military.
    
    `US_MILITARY_CLES`: A Civilian Leave and Earnings Statment (CLES) issued by the US military.
    
    `GIG`: Used to indicate that the income is related to gig work. Does not necessarily correspond to a specific document type.
    
    `NONE`: Used to indicate that there is no underlying document for the data.
    
    `UNKNOWN`: Document type could not be determined."""

    status: Optional[str] = None
    """The processing status of the document."""

    download_url: Optional[str] = None
    """Signed URL to retrieve the underlying file."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditDocumentMetadata":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditDocumentMetadata":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
