from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class WalletTransactionStatus(str, Enum):
    initiated = "INITIATED"
    executed = "EXECUTED"
    blocked = "BLOCKED"
    failed = "FAILED"
