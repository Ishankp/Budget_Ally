from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .sandbox_public_token_create_request_options_transactions import SandboxPublicTokenCreateRequestOptionsTransactions


class SandboxPublicTokenCreateRequestOptions(BaseModel):
    webhook: Optional[str] = None
    """Specify a webhook to associate with the new Item."""

    override_username: Optional[str] = None
    """Test username to use for the creation of the Sandbox Item. Default value is `user_good`."""

    override_password: Optional[str] = None
    """Test password to use for the creation of the Sandbox Item. Default value is `pass_good`."""

    transactions: Optional[SandboxPublicTokenCreateRequestOptionsTransactions] = None
    """An optional set of parameters corresponding to transactions options."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "SandboxPublicTokenCreateRequestOptions":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "SandboxPublicTokenCreateRequestOptions":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
