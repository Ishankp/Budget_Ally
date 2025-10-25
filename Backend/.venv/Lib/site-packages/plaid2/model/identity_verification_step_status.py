from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class IdentityVerificationStepStatus(str, Enum):
    success = "success"
    active = "active"
    failed = "failed"
    waiting_for_prerequisite = "waiting_for_prerequisite"
    not_applicable = "not_applicable"
    skipped = "skipped"
    expired = "expired"
    canceled = "canceled"
    pending_review = "pending_review"
    manually_approved = "manually_approved"
    manually_rejected = "manually_rejected"
