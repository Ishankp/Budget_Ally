from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class CustomerInitiatedReturnRisk(BaseModel):
    score: int
    """A score from 0-99 that indicates the transaction return risk: a higher risk score suggests a higher return likelihood."""

    risk_tier: int
    """A tier corresponding to the projected likelihood that the transaction, if initiated, will be subject to a return.
    
    In the `customer_initiated_return_risk` object, there are five risk tiers corresponding to the scores:
      1: Predicted customer-initiated return incidence rate between 0.00% - 0.02%
      2: Predicted customer-initiated return incidence rate between 0.02% - 0.05%
      3: Predicted customer-initiated return incidence rate between 0.05% - 0.1%
      4: Predicted customer-initiated return incidence rate between 0.1% - 0.5%
      5: Predicted customer-initiated return incidence rate greater than 0.5%
    """

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CustomerInitiatedReturnRisk":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CustomerInitiatedReturnRisk":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
