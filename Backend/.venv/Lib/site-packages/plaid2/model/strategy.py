from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class Strategy(str, Enum):
    reset = "reset"
    incomplete = "incomplete"
    infer = "infer"
    custom = "custom"
