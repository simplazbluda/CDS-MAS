import chromadb

from ai.rag.embeddings import EmbeddingModel


class MedicalKnowledgeBase:


    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./medical_db"
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="medical_documents"
            )
        )

        self.embedding_model = EmbeddingModel()



    def add_document(
        self,
        document_id,
        text
    ):

        embedding = (
            self.embedding_model.encode(text)
        )


        self.collection.add(
            ids=[document_id],
            documents=[text],
            embeddings=[
                embedding.tolist()
            ]
        )



    def search(
        self,
        query
    ):

        embedding = (
            self.embedding_model.encode(query)
        )


        result = self.collection.query(
            query_embeddings=[
                embedding.tolist()
            ],
            n_results=3
        )

        return result["documents"]