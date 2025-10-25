from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class DocumentRiskSignal(BaseModel):
    signal_description: Optional[str] = None
    """A human-readable explanation providing more detail into the particular risk signal"""

    actual_value: Optional[str] = None
    """The derived value obtained in the risk signal calculation process for this field"""

    has_fraud_risk: Optional[bool] = None
    """A flag used to quickly identify if the signal indicates that this field is authentic or fraudulent"""

    institution_metadata: Optional[str] = None
    """An object which contains additional metadata about the institution used to compute the verification attribute"""

    field: Optional[str] = None
    """The field which the risk signal was computed for"""

    expected_value: Optional[str] = None
    """The expected value of the field, as seen on the document"""

    type: Optional[str] = None
    """The result from the risk signal check."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "DocumentRiskSignal":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "DocumentRiskSignal":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
