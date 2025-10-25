from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class BankInitiatedReturnRisk(BaseModel):
    risk_tier: int
    """In the `bank_initiated_return_risk` object, there are eight risk tiers corresponding to the scores:
      1: Predicted bank-initiated return incidence rate between 0.0% - 0.5%
      2: Predicted bank-initiated return incidence rate between 0.5% - 1.5%
      3: Predicted bank-initiated return incidence rate between 1.5% - 3%
      4: Predicted bank-initiated return incidence rate between 3% - 5%
      5: Predicted bank-initiated return incidence rate between 5% - 10%
      6: Predicted bank-initiated return incidence rate between 10% - 15%
      7: Predicted bank-initiated return incidence rate between 15% and 50%
      8: Predicted bank-initiated return incidence rate greater than 50%
    """

    score: int
    """A score from 0-99 that indicates the transaction return risk: a higher risk score suggests a higher return likelihood."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "BankInitiatedReturnRisk":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "BankInitiatedReturnRisk":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
