from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransferStatus(str, Enum):
    pending = "pending"
    posted = "posted"
    cancelled = "cancelled"
    failed = "failed"
    returned = "returned"
