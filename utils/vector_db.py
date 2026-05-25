from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from typing import List

class VectorDB:
    def __init__(self, api_key: str):
        self.embeddings = OpenAIEmbeddings(openai_api_key=api_key)
        self.vectorstore = None

    def create_vectorstore(self, chunks: List[str]):
        """
        Create FAISS vectorstore from document chunks.
        """
        self.vectorstore = FAISS.from_texts(chunks, self.embeddings)

    def get_retriever(self, k: int = 5):
        """
        Get a retriever for similarity search.
        """
        if self.vectorstore is None:
            raise ValueError("Vectorstore not created. Call create_vectorstore first.")
        return self.vectorstore.as_retriever(search_kwargs={"k": k})

    def get_context(self, query: str, k: int = 5) -> str:
        """
        Retrieve relevant context from the vectorstore.
        """
        if self.vectorstore is None:
            raise ValueError("Vectorstore not created. Call create_vectorstore first.")
        docs = self.vectorstore.similarity_search(query, k=k)
        return "\n".join([doc.page_content for doc in docs])
