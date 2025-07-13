from src.github.data_model import Data
from sentence_transformers import SentenceTransformer
import numpy as np
import textwrap


class Embedding:
    def __init__(self):
        self.docs_embed = None  # nd array with embedding
        self.appended_q_a_list = (
            None  # qa docs array to get the embeddings back to data
        )
        self.model = SentenceTransformer(
            "Alibaba-NLP/gte-base-en-v1.5", trust_remote_code=True
        )

    def create_embedding(self, data: Data):
        self.appended_q_a_list = []
        for question in data.questions:
            answers = question.answers
            # we are appending each question to each answer in a discussion
            self.appended_q_a_list.extend(
                [question.question + "\n\n\n" + answer.ans for answer in answers]
            )
            self.docs_embed = self.model.encode(
                self.appended_q_a_list, normalize_embeddings=True
            )

    def fetch_document(self, query: str, top_n=3):
        query_embed = self.model.encode(query, normalize_embeddings=True)
        similarities = np.dot(self.docs_embed, query_embed.T)
        top_idx = np.argsort(similarities, axis=0)[-top_n:][::-1].tolist()
        most_similar_documents = [self.appended_q_a_list[idx] for idx in top_idx]

        # TODO: Move this to a different function
        CONTEXT = ""
        for i, p in enumerate(most_similar_documents):
            wrapped_text = textwrap.fill(p, width=100)
            CONTEXT += wrapped_text + "\n\n"
        return CONTEXT
