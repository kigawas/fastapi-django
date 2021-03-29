from typing import List

from fastapi import APIRouter, Depends

from polls import adapters
from polls.models import Choice
from polls.schemas import FastChoice, FastChoices

router = APIRouter()


@router.get("/")
def get_choices(
    choices: List[Choice] = Depends(adapters.retrieve_choices),
) -> FastChoices:
    return FastChoices.from_qs(choices)


@router.get("/{c_id}")
def get_choice(choice: Choice = Depends(adapters.retrieve_choice)) -> FastChoice:
    return FastChoice.from_orm(choice)
