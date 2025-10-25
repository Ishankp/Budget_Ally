from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_card_liability import CreditCardLiability
from .mortgage_liability import MortgageLiability
from .student_loan import StudentLoan


class LiabilitiesObject(BaseModel):
    mortgage: Optional[List[MortgageLiability]] = None
    """The mortgage accounts returned."""

    credit: Optional[List[CreditCardLiability]] = None
    """The credit accounts returned."""

    student: Optional[List[StudentLoan]] = None
    """The student loan accounts returned."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LiabilitiesObject":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "LiabilitiesObject":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
