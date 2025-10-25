from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .wallet_transaction_amount import WalletTransactionAmount
from .wallet_transaction_counterparty import WalletTransactionCounterparty


class WalletTransactionExecuteRequest(BaseModel):
    idempotency_key: str
    """A random key provided by the client, per unique wallet transaction. Maximum of 128 characters.
    
    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. If a request to execute a wallet transaction fails due to a network connection error, then after a minimum delay of one minute, you can retry the request with the same idempotency key to guarantee that only a single wallet transaction is created. If the request was successfully processed, it will prevent any transaction that uses the same idempotency key, and was received within 24 hours of the first request, from being processed."""

    wallet_id: str
    """The ID of the e-wallet to debit from"""

    counterparty: WalletTransactionCounterparty
    """An object representing the e-wallet transaction's counterparty"""

    amount: WalletTransactionAmount
    """The amount and currency of a transaction"""

    reference: str
    """A reference for the transaction. This must be an alphanumeric string with at most 18 characters and must not contain any special characters or spaces."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "WalletTransactionExecuteRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "WalletTransactionExecuteRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
