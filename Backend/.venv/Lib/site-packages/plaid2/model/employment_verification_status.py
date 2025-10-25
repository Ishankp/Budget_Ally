from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class EmploymentVerificationStatus(str, Enum):
    employment_status_active = "EMPLOYMENT_STATUS_ACTIVE"
    employment_status_inactive = "EMPLOYMENT_STATUS_INACTIVE"
