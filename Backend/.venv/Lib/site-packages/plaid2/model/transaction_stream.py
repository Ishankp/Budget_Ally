from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .personal_finance_category import PersonalFinanceCategory
from .transaction_stream_amount import TransactionStreamAmount


class TransactionStream(BaseModel):
    frequency: str
    """Describes the frequency of the transaction stream.
    
    `WEEKLY`: Assigned to a transaction stream that occurs approximately every week.
    
    `BIWEEKLY`: Assigned to a transaction stream that occurs approximately every 2 weeks.
    
    `SEMI_MONTHLY`: Assigned to a transaction stream that occurs approximately twice per month. This frequency is typically seen for inflow transaction streams.
    
    `MONTHLY`: Assigned to a transaction stream that occurs approximately every month.
    
    `UNKNOWN`: Assigned to a transaction stream that does not fit any of the pre-defined frequencies."""

    stream_id: str
    """A unique id for the stream"""

    is_active: bool
    """Indicates whether the transaction stream is still live."""

    first_date: str
    """The posted date of the earliest transaction in the stream."""

    account_id: str
    """The ID of the account to which the stream belongs"""

    average_amount: TransactionStreamAmount
    """Object with data pertaining to an amount on the transaction stream."""

    description: str
    """A description of the transaction stream."""

    category: List[str]
    """A hierarchical array of the categories to which this transaction belongs. See [Categories](https://plaid.com/docs/#category-overview)."""

    transaction_ids: List[str]
    """An array of Plaid transaction IDs belonging to the stream, sorted by posted date."""

    last_date: str
    """The posted date of the latest transaction in the stream."""

    merchant_name: Optional[str] = None
    """The merchant associated with the transaction stream."""

    last_amount: TransactionStreamAmount
    """Object with data pertaining to an amount on the transaction stream."""

    status: str
    """The current status of the transaction stream.
    
    `MATURE`: A `MATURE` recurring stream should have at least 3 transactions and happen on a regular cadence.
    
    `EARLY_DETECTION`: When a recurring transaction first appears in the transaction history and before it fulfills the requirement of a mature stream, the status will be `EARLY_DETECTION`.
    
    `TOMBSTONED`: A stream that was previously in the `EARLY_DETECTION` status will move to the `TOMBSTONED` status when no further transactions were found at the next expected date.
    
    `UNKNOWN`: A stream is assigned an `UNKNOWN` status when none of the other statuses are applicable."""

    category_id: str
    """The ID of the category to which this transaction belongs. See [Categories](https://plaid.com/docs/#category-overview)."""

    personal_finance_category: Optional[PersonalFinanceCategory] = None
    """Information describing the intent of the transaction. Most relevant for personal finance use cases, but not limited to such use cases.
    
    See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransactionStream":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransactionStream":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
