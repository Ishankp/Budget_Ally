from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class VerificationRefreshStatus(str, Enum):
    verification_refresh_status_user_presence_required = "VERIFICATION_REFRESH_STATUS_USER_PRESENCE_REQUIRED"
    verification_refresh_successful = "VERIFICATION_REFRESH_SUCCESSFUL"
    verification_refresh_not_found = "VERIFICATION_REFRESH_NOT_FOUND"
