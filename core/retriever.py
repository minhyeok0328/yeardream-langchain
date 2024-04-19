from typing import Type
from core.db import VectorStore

class Retriever:
    def __init__(self, db: Type[VectorStore], k: int = 1):
        self.k = k
        self.db = db

    def find_related_knowledge(self, user_input: str) -> str:
        related_knowledge = self.db.query(text=user_input, k=self.k)

        return related_knowledge