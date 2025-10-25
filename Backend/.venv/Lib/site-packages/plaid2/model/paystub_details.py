from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PaystubDetails(BaseModel):
    paystub_provider: Optional[str] = None
    """The name of the payroll provider that generated the paystub, e.g. ADP"""

    pay_date: Optional[str] = None
    """Pay date on the paystub in the 'YYYY-MM-DD' format."""

    pay_period_end_date: Optional[str] = None
    """Ending date of the pay period on the paystub in the 'YYYY-MM-DD' format."""

    pay_period_start_date: Optional[str] = None
    """Beginning date of the pay period on the paystub in the 'YYYY-MM-DD' format."""

    pay_frequency: Optional[str] = None
    """The frequency at which the employee is paid. Possible values: `MONTHLY`, `BI-WEEKLY`, `WEEKLY`, `SEMI-MONTHLY`."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaystubDetails":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PaystubDetails":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
