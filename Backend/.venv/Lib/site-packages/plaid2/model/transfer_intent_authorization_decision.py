from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransferIntentAuthorizationDecision(str, Enum):
    approved = "APPROVED"
    declined = "DECLINED"
