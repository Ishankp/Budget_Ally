from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class CountryCode(str, Enum):
    us = "US"
    gb = "GB"
    es = "ES"
    nl = "NL"
    fr = "FR"
    ie = "IE"
    ca = "CA"
    de = "DE"
    it = "IT"
