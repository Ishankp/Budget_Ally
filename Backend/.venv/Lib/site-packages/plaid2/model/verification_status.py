from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class VerificationStatus(str, Enum):
    verified = "VERIFIED"
    unverified = "UNVERIFIED"
    needs_info = "NEEDS_INFO"
    unable_to_verify = "UNABLE_TO_VERIFY"
    unknown = "UNKNOWN"
