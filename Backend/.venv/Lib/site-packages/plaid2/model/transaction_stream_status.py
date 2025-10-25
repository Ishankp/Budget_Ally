from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransactionStreamStatus(str, Enum):
    unknown = "UNKNOWN"
    mature = "MATURE"
    early_detection = "EARLY_DETECTION"
    tombstoned = "TOMBSTONED"
