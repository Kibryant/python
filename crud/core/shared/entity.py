from uuid import uuid4
from abc import ABC


class Entity(ABC):
    def __init__(self, id: str | None):
        self.id = id or str(uuid4())
