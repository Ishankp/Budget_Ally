from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransferSweepStatus(str, Enum):
    unswept = "unswept"
    swept = "swept"
    reverse_swept = "reverse_swept"
    return_swept = "return_swept"
