from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .signal_evaluate_core_attributes import SignalEvaluateCoreAttributes
from .signal_scores import SignalScores


class SignalEvaluateResponse(BaseModel):
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""

    scores: SignalScores
    """Risk scoring details broken down by risk category."""

    core_attributes: Optional[SignalEvaluateCoreAttributes] = None
    """The core attributes object contains additional data that can be used to assess the ACH return risk. Examples of data include:
    
    `days_since_first_plaid_connection`: The number of days since the first time the Item was connected to an application via Plaid
    `plaid_connections_count_7d`: The number of times the Item has been connected to applications via Plaid over the past 7 days
    `plaid_connections_count_30d`: The number of times the Item has been connected to applications via Plaid over the past 30 days
    `total_plaid_connections_count`: The number of times the Item has been connected to applications via Plaid
    `is_savings_or_money_market_account`: Indicates whether the ACH transaction funding account is a savings/money market account
    
    For the full list and detailed documentation of core attributes available, or to request that core attributes not be returned, contact Sales or your Plaid account manager"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "SignalEvaluateResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "SignalEvaluateResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
