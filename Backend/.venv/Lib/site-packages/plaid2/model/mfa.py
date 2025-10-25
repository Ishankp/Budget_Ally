from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class Mfa(BaseModel):
    question_rounds: float
    """Number of rounds of questions. Required if value of `type` is `questions`. """

    questions_per_round: float
    """Number of questions per round. Required if value of `type` is `questions`. If value of type is `selections`, default value is 2."""

    selection_rounds: float
    """Number of rounds of selections, used if `type` is `selections`. Defaults to 1."""

    selections_per_question: float
    """Number of available answers per question, used if `type` is `selection`. Defaults to 2.
    """

    type: str
    """Possible values are `device`, `selections`, or `questions`.
    
    If value is `device`, the MFA answer is `1234`.
    
    If value is `selections`, the MFA answer is always the first option.
    
    If value is `questions`, the MFA answer is  `answer_<i>_<j>` for the j-th question in the i-th round, starting from 0. For example, the answer to the first question in the second round is `answer_1_0`."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Mfa":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Mfa":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
