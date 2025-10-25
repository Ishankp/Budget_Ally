from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class CreditBankIncomeErrorType(str, Enum):
    internal_server_error = "INTERNAL_SERVER_ERROR"
    insufficient_credentials = "INSUFFICIENT_CREDENTIALS"
    item_locked = "ITEM_LOCKED"
    user_setup_required = "USER_SETUP_REQUIRED"
    country_not_supported = "COUNTRY_NOT_SUPPORTED"
    institution_down = "INSTITUTION_DOWN"
    institution_no_longer_supported = "INSTITUTION_NO_LONGER_SUPPORTED"
    institution_not_responding = "INSTITUTION_NOT_RESPONDING"
    invalid_credentials = "INVALID_CREDENTIALS"
    invalid_mfa = "INVALID_MFA"
    invalid_send_method = "INVALID_SEND_METHOD"
    item_login_required = "ITEM_LOGIN_REQUIRED"
    mfa_not_supported = "MFA_NOT_SUPPORTED"
    no_accounts = "NO_ACCOUNTS"
    item_not_supported = "ITEM_NOT_SUPPORTED"
    access_not_granted = "ACCESS_NOT_GRANTED"
