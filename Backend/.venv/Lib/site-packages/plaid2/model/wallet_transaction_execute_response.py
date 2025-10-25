from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class WalletTransactionExecuteResponse(BaseModel):
    transaction_id: str
    """A unique ID identifying the transaction"""

    status: str
    """The status of the transaction.
    
    `INITIATED`: This is the initial state of all transactions. It indicates that the transaction has been initiated and is currently being processed.
    
    `EXECUTED`: The transaction has been successfully executed.
    
    `FAILED`: The transaction failed to process successfully. This is a terminal status.
    
    `BLOCKED`: The transaction has been blocked for violating compliance rules. This is a terminal status."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "WalletTransactionExecuteResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "WalletTransactionExecuteResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
