from datetime import datetime
from typing import List

from pydantic import BaseModel

from polls.models import Question


class FastQuestion(BaseModel):
    question_text: str
    pub_date: datetime

    @classmethod
    def from_model(cls, instance: Question):
        return cls(
            id=instance.id,
            question_text=instance.question_text,
            pub_date=instance.pub_date,
        )


class FastQuestions(BaseModel):
    items: List[FastQuestion]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=[FastQuestion.from_model(i) for i in qs])
