from embeddings import Embedding
from data_model import Data, Question, Answer

question_1 = Question(
    id="1",
    question="what is the color of sky",
    answers=[
        Answer(ans="sky is usually blue"),
        Answer(ans="when it's cloudy it's grey"),
    ],
)
question_2 = Question(
    id="2",
    question="When is tamil new year",
    answers=[
        Answer(ans="it's 14th apr every year"),
        Answer(ans="one political party says it's on the thai tamil month"),
        Answer(ans="nobody knows anymore"),
    ],
)
data = Data(questions=[question_1, question_2])
embedding_obj = Embedding(data)
answer = embedding_obj.fetch_document("what is the color of sky")
print(answer)
