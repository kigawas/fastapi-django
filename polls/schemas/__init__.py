from datetime import datetime
from typing import List

from django.db import models
from pydantic import BaseModel as _BaseModel
from pydantic import ConfigDict


class BaseModel(_BaseModel):
    @classmethod
    def from_orms(cls, instances: List[models.Model]):
        return [cls.model_validate(inst) for inst in instances]


class FastQuestion(BaseModel):
    question_text: str
    pub_date: datetime
    model_config = ConfigDict(from_attributes=True)


class FastQuestions(BaseModel):
    items: List[FastQuestion]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=FastQuestion.from_orms(qs))


class FastChoice(BaseModel):
    question: FastQuestion
    choice_text: str
    model_config = ConfigDict(from_attributes=True)


class FastChoices(BaseModel):
    items: List[FastChoice]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=FastChoice.from_orms(qs))
