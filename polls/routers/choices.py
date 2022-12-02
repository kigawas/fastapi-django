from typing import List

from fastapi import APIRouter, Depends

from polls import adapters
from polls.models import Choice
from polls.schemas import FastChoice, FastChoices

router = APIRouter(prefix="/choice", tags=["choices"])


@router.get("/", response_model=FastChoices)
def get_choices(
    choices: List[Choice] = Depends(adapters.retrieve_choices),
) -> FastChoices:
    return FastChoices.from_qs(choices)


@router.get("/{c_id}", response_model=FastChoice)
def get_choice(choice: Choice = Depends(adapters.retrieve_choice)) -> FastChoice:
    return FastChoice.from_orm(choice)
