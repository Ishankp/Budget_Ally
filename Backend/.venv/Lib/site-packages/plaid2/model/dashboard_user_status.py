from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class DashboardUserStatus(str, Enum):
    invited = "invited"
    active = "active"
    deactivated = "deactivated"
