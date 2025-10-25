from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class ProgramNameSensitivity(str, Enum):
    coarse = "coarse"
    balanced = "balanced"
    strict = "strict"
    exact = "exact"
