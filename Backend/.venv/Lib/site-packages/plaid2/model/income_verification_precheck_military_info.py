from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class IncomeVerificationPrecheckMilitaryInfo(BaseModel):
    branch: Optional[str] = None
    """If the user is currently serving in the US military, the branch of the military in which they are serving
    Valid values: 'AIR FORCE', 'ARMY', 'COAST GUARD', 'MARINES', 'NAVY', 'UNKNOWN'"""

    is_active_duty: Optional[bool] = None
    """Is the user currently active duty in the US military"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IncomeVerificationPrecheckMilitaryInfo":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "IncomeVerificationPrecheckMilitaryInfo":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
