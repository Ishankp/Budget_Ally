from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class WebhookType(str, Enum):
    auth = "AUTH"
    holdings = "HOLDINGS"
    investments_transactions = "INVESTMENTS_TRANSACTIONS"
    item = "ITEM"
    liabilities = "LIABILITIES"
    transactions = "TRANSACTIONS"
