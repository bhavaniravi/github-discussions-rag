import chromadb
from data_model import Data


class ChromaEmbedding:
    def __init__(self, collection_name="discussions"):
        self.chroma_client = chromadb.PersistentClient(path=f"data/{collection_name}")
        self.embedding_exists = False
        try:
            self.collection = self.chroma_client.get_collection(collection_name)
            self.embedding_exists = True
        except:
            self.collection = self.chroma_client.create_collection(collection_name)

    def create_embedding(self, data: Data):
        self.appended_q_a_list = []

        for question in data.questions:
            answers = question.answers
            if not answers:
                continue
            # we are appending each question to each answer in a discussion
            q_a_list = []
            q_a_id = []
            for answer in answers:
                q_a_list.append(question.question + '\n\n\n'+ answer.ans)
                q_a_id.append(question.id + '_' + answer.id)

            self.collection.add(
                documents=q_a_list,
                ids=q_a_id
            )


    def fetch_document(self, query: str, top_n=3):
        results = self.collection.query(
            query_texts=[query], # Chroma will embed this for you
            n_results=top_n # how many results to return
        )
        print(results)
        return results["documents"][:top_n]
