from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class Form1099Type(str, Enum):
    form_1099_type_unknown = "FORM_1099_TYPE_UNKNOWN"
    form_1099_type_misc = "FORM_1099_TYPE_MISC"
    form_1099_type_k = "FORM_1099_TYPE_K"
