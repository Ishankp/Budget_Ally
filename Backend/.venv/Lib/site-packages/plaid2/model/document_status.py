from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class DocumentStatus(str, Enum):
    success = "success"
    failed = "failed"
    manually_approved = "manually_approved"
