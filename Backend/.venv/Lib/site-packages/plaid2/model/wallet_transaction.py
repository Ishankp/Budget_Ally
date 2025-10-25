from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .wallet_transaction_amount import WalletTransactionAmount
from .wallet_transaction_counterparty import WalletTransactionCounterparty


class WalletTransaction(BaseModel):
    status: str
    """The status of the transaction.
    
    `INITIATED`: This is the initial state of all transactions. It indicates that the transaction has been initiated and is currently being processed.
    
    `EXECUTED`: The transaction has been successfully executed.
    
    `FAILED`: The transaction failed to process successfully. This is a terminal status.
    
    `BLOCKED`: The transaction has been blocked for violating compliance rules. This is a terminal status."""

    created_at: str
    """Timestamp when the transaction was created, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format."""

    transaction_id: str
    """A unique ID identifying the transaction"""

    type: str
    """The type of the transaction. The supported transaction types that are returned are:
    `BANK_TRANSFER:` a transaction which credits an e-wallet through an external bank transfer.
    
    `PAYOUT:` a transaction which debits an e-wallet by disbursing funds to a counterparty.
    
    `PIS_PAY_IN:` a payment which credits an e-wallet through Plaid's Payment Initiation Services (PIS) APIs. For more information see the [Payment Initiation endpoints](https://plaid.com/docs/api/products/payment-initiation/).
    
    `REFUND:` a transaction which debits an e-wallet by refunding a previously initated payment made through Plaid's [PIS APIs](https://plaid.com/docs/api/products/payment-initiation/)."""

    reference: str
    """A reference for the transaction"""

    counterparty: WalletTransactionCounterparty
    """An object representing the e-wallet transaction's counterparty"""

    amount: WalletTransactionAmount
    """The amount and currency of a transaction"""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "WalletTransaction":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "WalletTransaction":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
