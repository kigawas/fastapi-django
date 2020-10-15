from datetime import datetime
from typing import List

from django.db import models
from pydantic import BaseModel as _BaseModel


class BaseModel(_BaseModel):
    @classmethod
    def from_model(cls, instance: models.Model):
        kwargs = {}
        for k, v in cls.__fields__.items():
            instance_attr = getattr(instance, k)
            if isinstance(instance_attr, models.Model):
                instance_attr = v.type_.from_model(instance_attr)
            kwargs[k] = instance_attr

        return cls(**kwargs)

    @classmethod
    def from_models(cls, instances: List[models.Model]):
        return [cls.from_model(inst) for inst in instances]


class FastQuestion(BaseModel):
    question_text: str
    pub_date: datetime


class FastQuestions(BaseModel):
    items: List[FastQuestion]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=FastQuestion.from_models(qs))


class FastChoice(BaseModel):
    question: FastQuestion
    choice_text: str


class FastChoices(BaseModel):
    items: List[FastChoice]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=FastChoice.from_models(qs))
