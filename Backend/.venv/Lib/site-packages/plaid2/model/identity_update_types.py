from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class IdentityUpdateTypes(str, Enum):
    phones = "PHONES"
    addresses = "ADDRESSES"
    emails = "EMAILS"
    names = "NAMES"
