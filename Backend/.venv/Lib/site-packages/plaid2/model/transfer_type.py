from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransferType(str, Enum):
    debit = "debit"
    credit = "credit"
