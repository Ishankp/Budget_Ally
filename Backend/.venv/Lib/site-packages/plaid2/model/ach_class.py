from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class AchClass(str, Enum):
    ccd = "ccd"
    ppd = "ppd"
    tel = "tel"
    web = "web"
