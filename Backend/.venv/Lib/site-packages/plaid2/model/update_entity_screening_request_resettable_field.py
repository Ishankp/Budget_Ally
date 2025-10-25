from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class UpdateEntityScreeningRequestResettableField(str, Enum):
    assignee = "assignee"
