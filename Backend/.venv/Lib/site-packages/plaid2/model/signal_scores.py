from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .bank_initiated_return_risk import BankInitiatedReturnRisk
from .customer_initiated_return_risk import CustomerInitiatedReturnRisk


class SignalScores(BaseModel):
    bank_initiated_return_risk: Optional[BankInitiatedReturnRisk] = None
    """The object contains a risk score and a risk tier that evaluate the transaction return risk because an account is overdrawn or because an ineligible account is used. Common return codes in this category include: "R01", "R02", "R03", "R04", "R06", "R08",  "R09", "R13", "R16", "R17", "R20", "R23". These returns have a turnaround time of 2 banking days."""

    customer_initiated_return_risk: Optional[CustomerInitiatedReturnRisk] = None
    """The object contains a risk score and a risk tier that evaluate the transaction return risk of an unauthorized debit. Common return codes in this category include: "R05", "R07", "R10", "R11", "R29". These returns typically have a return time frame of up to 60 calendar days. During this period, the customer of financial institutions can dispute a transaction as unauthorized."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "SignalScores":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "SignalScores":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
