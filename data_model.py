from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Answer:
    id: str
    ans: str

@dataclass
class Question:
    id: str
    question: str 
    answers: List[Answer]

@dataclass
class Data:
    questions: Dict[Question, List[Answer]] = None