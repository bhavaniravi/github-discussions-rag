from typing import List, Dict

class Answer:
    id: str
    ans: str

class Question:
    id: str
    question: str 
    answers: List[Answer]

class Data:
    questions: Dict[Question, List[Answer]] = None