from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class CreditBankIncomeWarningCode(str, Enum):
    identity_unavailable = "IDENTITY_UNAVAILABLE"
    transactions_unavailable = "TRANSACTIONS_UNAVAILABLE"
    item_unapproved = "ITEM_UNAPPROVED"
    report_deleted = "REPORT_DELETED"
