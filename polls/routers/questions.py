from typing import List

from fastapi import APIRouter, Depends

from polls import adapters
from polls.models import Question
from polls.schemas import FastQuestion, FastQuestions

router = APIRouter(prefix="/question", tags=["questions"])


@router.get("/", response_model=FastQuestions)
def get_questions(
    questions: List[Question] = Depends(adapters.retrieve_questions),
) -> FastQuestions:
    return FastQuestions.from_qs(questions)


@router.get("/{q_id}", response_model=FastQuestion)
def get_question(
    question: Question = Depends(adapters.retrieve_question),
) -> FastQuestion:
    return FastQuestion.from_orm(question)
