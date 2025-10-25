from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .transfer_sweep import TransferSweep


class TransferSweepGetResponse(BaseModel):
    sweep: TransferSweep
    """Describes a sweep of funds to / from the sweep account.
    
    A sweep is associated with many sweep events (events of type `swept` or `return_swept`) which can be retrieved by invoking the `/transfer/event/list` endpoint with the corresponding `sweep_id`.
    
    `swept` events occur when the transfer amount is credited or debited from your sweep account, depending on the `type` of the transfer. `return_swept` events occur when a transfer is returned and Plaid undoes the credit or debit.
    
    The total sum of the `swept` and `return_swept` events is equal to the `amount` of the sweep Plaid creates and matches the amount of the entry on your sweep account ledger."""

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
    def parse_obj(cls, data: Any) -> "TransferSweepGetResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransferSweepGetResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
