from typing import List, Dict
from dataclasses import dataclass


@dataclass
class Answer:
    ans: str
    id: str = None

@dataclass
class Question:
    question: str 
    answers: List[Answer]
    id: str = None

@dataclass
class Data:
    questions: Dict[Question, List[Answer]] = None