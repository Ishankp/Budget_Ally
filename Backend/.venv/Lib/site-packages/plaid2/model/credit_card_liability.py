from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .apr import Apr


class CreditCardLiability(BaseModel):
    minimum_payment_amount: Optional[float] = None
    """The minimum payment due for the next billing cycle."""

    last_statement_balance: Optional[float] = None
    """The total amount owed as of the last statement issued"""

    account_id: Optional[str] = None
    """The ID of the account that this liability belongs to."""

    last_payment_amount: Optional[float] = None
    """The amount of the last payment."""

    next_payment_due_date: Optional[str] = None
    """The due date for the next payment. The due date is `null` if a payment is not expected. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""

    is_overdue: Optional[bool] = None
    """true if a payment is currently overdue. Availability for this field is limited."""

    aprs: List[Apr]
    """The various interest rates that apply to the account. APR information is not provided by all card issuers; if APR data is not available, this array will be empty."""

    last_payment_date: Optional[str] = None
    """The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). Availability for this field is limited."""

    last_statement_issue_date: Optional[str] = None
    """The date of the last statement. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD)."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditCardLiability":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditCardLiability":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
