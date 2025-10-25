from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class RelayEvent(str, Enum):
    get_called = "GET_CALLED"
    refresh_called = "REFRESH_CALLED"
    audit_copy_create_called = "AUDIT_COPY_CREATE_CALLED"
