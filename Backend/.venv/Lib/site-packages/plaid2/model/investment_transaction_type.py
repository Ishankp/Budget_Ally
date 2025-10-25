from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class InvestmentTransactionType(str, Enum):
    buy = "buy"
    sell = "sell"
    cancel = "cancel"
    cash = "cash"
    fee = "fee"
    transfer = "transfer"
