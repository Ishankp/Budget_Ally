from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransferIntentCreateMode(str, Enum):
    payment = "PAYMENT"
    disbursement = "DISBURSEMENT"
