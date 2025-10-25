from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransferAuthorizationGuaranteeDecision(str, Enum):
    guaranteed = "GUARANTEED"
    not_guaranteed = "NOT_GUARANTEED"
