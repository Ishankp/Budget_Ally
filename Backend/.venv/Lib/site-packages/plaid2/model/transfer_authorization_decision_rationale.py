from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransferAuthorizationDecisionRationale(BaseModel):
    description: str
    """A human-readable description of the code associated with a transfer approval or transfer decline."""

    code: str
    """A code representing the rationale for approving or declining the proposed transfer. Possible values are:
    
    `MANUALLY_VERIFIED_ITEM` – Item created via same-day micro deposits, limited information available. Plaid will offer `approved` as a transaction decision.
    
    `LOGIN_REQUIRED` – Unable to collect the account information due to Item staleness. Can be rectified using Link in update mode. Plaid will offer `approved` as a transaction decision.
    
    `ERROR` – Unable to collect the account information due to an error. Plaid will offer `approved` as a transaction decision.
    
    `NSF` – Transaction likely to result in a return due to insufficient funds. Plaid will offer `declined` as a transaction decision.
    
    `RISK` - Transaction is high-risk. Plaid will offer `declined` as a transaction decision.
    
    `TRANSFER_LIMIT_REACHED` - One or several transfer limits are reached, e.g. monthly transfer limit. Plaid will offer `declined` as a transaction decision."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferAuthorizationDecisionRationale":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransferAuthorizationDecisionRationale":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
