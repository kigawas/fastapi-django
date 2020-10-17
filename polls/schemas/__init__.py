from datetime import datetime
from typing import List

from django.db import models
from pydantic import BaseModel as _BaseModel


class BaseModel(_BaseModel):
    @classmethod
    def from_orms(cls, instances: List[models.Model]):
        return [cls.from_orm(inst) for inst in instances]


class FastQuestion(BaseModel):
    question_text: str
    pub_date: datetime

    class Config:
        orm_mode = True


class FastQuestions(BaseModel):
    items: List[FastQuestion]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=FastQuestion.from_orms(qs))


class FastChoice(BaseModel):
    question: FastQuestion
    choice_text: str

    class Config:
        orm_mode = True


class FastChoices(BaseModel):
    items: List[FastChoice]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=FastChoice.from_orms(qs))
