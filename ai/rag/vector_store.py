"""
Medical Knowledge Vector Store

Responsible for:

- storing medical documents
- generating embeddings
- semantic retrieval
"""


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





    # -----------------------------------
    # Add Medical Document
    # -----------------------------------

    def add_document(
        self,
        document_id: str,
        text: str,
        metadata: dict = None
    ):


        embedding = (

            self.embedding_model.encode(text)

        )



        self.collection.upsert(

            ids=[document_id],


            documents=[text],


            embeddings=[

                embedding.tolist()

            ],


            metadatas=[

                metadata if metadata else {}

            ]

        )





    # -----------------------------------
    # Search Medical Knowledge
    # -----------------------------------

    def search(
        self,
        query: str,
        n_results: int = 3
    ):


        if not query:


            return []



        embedding = (

            self.embedding_model.encode(query)

        )



        result = self.collection.query(


            query_embeddings=[

                embedding.tolist()

            ],


            n_results=n_results,


            include=[

                "documents",

                "metadatas",

                "distances"

            ]

        )



        documents = result.get(

            "documents",

            []

        )



        if not documents:


            return []



        # Chroma returns nested list

        return documents[0]