from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class BankTransferEventType(str, Enum):
    pending = "pending"
    cancelled = "cancelled"
    failed = "failed"
    posted = "posted"
    reversed = "reversed"
