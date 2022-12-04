from typing import Type, TypeVar

from django.db import models
from fastapi import HTTPException, Path

from polls.models import Choice, Question

ModelT = TypeVar("ModelT", bound=models.Model)


async def retrieve_object(model_class: Type[ModelT], id: int) -> ModelT:
    instance = await model_class.objects.filter(pk=id).afirst()
    if not instance:
        raise HTTPException(status_code=404, detail="Object not found.")
    return instance


async def retrieve_question(q_id: int = Path(..., description="get question from db")):
    return await retrieve_object(Question, q_id)


async def retrieve_choice(c_id: int = Path(..., description="get choice from db")):
    return await retrieve_object(Choice, c_id)


async def retrieve_questions():
    return [q async for q in Question.objects.all()]


async def retrieve_choices():
    return [c async for c in Choice.objects.all()]
