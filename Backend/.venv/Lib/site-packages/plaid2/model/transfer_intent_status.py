from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransferIntentStatus(str, Enum):
    pending = "PENDING"
    succeeded = "SUCCEEDED"
    failed = "FAILED"
