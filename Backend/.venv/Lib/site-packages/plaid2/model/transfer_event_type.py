from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransferEventType(str, Enum):
    pending = "pending"
    cancelled = "cancelled"
    failed = "failed"
    posted = "posted"
    returned = "returned"
    swept = "swept"
    reverse_swept = "reverse_swept"
    return_swept = "return_swept"
