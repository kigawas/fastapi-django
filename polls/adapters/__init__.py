from typing import Type
from typing import TypeVar

from django.db import models
from fastapi import HTTPException
from fastapi import Path

from polls.models import Question


ModelT = TypeVar("ModelT", bound=models.Model)


def retieve_object(model_class: Type[ModelT], id: int) -> ModelT:
    instance = model_class.objects.filter(pk=id).first()
    if not instance:
        raise HTTPException(status_code=404, detail="Object not found.")
    return instance


def retrieve_question(
    q_id: int = Path(..., description="retrive question from db")
) -> Question:
    return retieve_object(Question, q_id)


def retrieve_questions():
    return Question.objects.all()
