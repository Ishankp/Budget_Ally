from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransactionCode(str, Enum):
    adjustment = "adjustment"
    atm = "atm"
    bank_charge = "bank charge"
    bill_payment = "bill payment"
    cash = "cash"
    cashback = "cashback"
    cheque = "cheque"
    direct_debit = "direct debit"
    interest = "interest"
    purchase = "purchase"
    standing_order = "standing order"
    transfer = "transfer"
