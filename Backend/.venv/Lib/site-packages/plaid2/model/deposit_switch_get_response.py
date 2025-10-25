from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class DepositSwitchGetResponse(BaseModel):
    amount_allocated: Optional[float] = None
    """The dollar amount of direct deposit allocated to the target account. Always `null` if the target account is not allocated an amount or if the deposit switch has not been completed."""

    account_has_multiple_allocations: Optional[bool] = None
    """When `true`, user’s direct deposit goes to multiple banks. When false, user’s direct deposit only goes to the target account. Always `null` if the deposit switch has not been completed."""

    institution_name: Optional[str] = None
    """The name of the institution selected by the user. If the user did not select an institution, the value returned is `null`."""

    target_item_id: Optional[str] = None
    """The ID of the Item the direct deposit was switched to."""

    target_account_id: Optional[str] = None
    """The ID of the bank account the direct deposit was switched to."""

    date_created: str
    """[ISO 8601](https://wikipedia.org/wiki/ISO_8601) date the deposit switch was created.
    """

    is_allocated_remainder: Optional[bool] = None
    """When `true`, the target account is allocated the remainder of direct deposit after all other allocations have been deducted. When `false`, user’s direct deposit is allocated as a percent or amount. Always `null` if the deposit switch has not been completed."""

    percent_allocated: Optional[float] = None
    """The percentage of direct deposit allocated to the target account. Always `null` if the target account is not allocated a percentage or if the deposit switch has not been completed or if `is_allocated_remainder` is true."""

    date_completed: Optional[str] = None
    """[ISO 8601](https://wikipedia.org/wiki/ISO_8601) date the deposit switch was completed. Always `null` if the deposit switch has not been completed.
    """

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""

    switch_method: Optional[str] = None
    """The method used to make the deposit switch.
    
    - `instant` – User instantly switched their direct deposit to a new or existing bank account by connecting their payroll or employer account.
    
    - `mail` – User requested that Plaid contact their employer by mail to make the direct deposit switch.
    
    - `pdf` – User generated a PDF or email to be sent to their employer with the information necessary to make the deposit switch.'"""

    employer_name: Optional[str] = None
    """The name of the employer selected by the user. If the user did not select an employer, the value returned is `null`."""

    employer_id: Optional[str] = None
    """The ID of the employer selected by the user. If the user did not select an employer, the value returned is `null`."""

    institution_id: Optional[str] = None
    """The ID of the institution selected by the user. If the user did not select an institution, the value returned is `null`."""

    state: str
    """
    The state, or status, of the deposit switch.
    
    - `initialized` – The deposit switch has been initialized with the user entering the information required to submit the deposit switch request.
    
    - `processing` – The deposit switch request has been submitted and is being processed.
    
    - `completed` – The user's employer has fulfilled the deposit switch request.
    
    - `error` – There was an error processing the deposit switch request."""

    deposit_switch_id: str
    """The ID of the deposit switch."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "DepositSwitchGetResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "DepositSwitchGetResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
