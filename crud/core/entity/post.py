from dataclasses import dataclass
from ..shared.entity import Entity
from datetime import datetime


@dataclass
class Post(Entity):
    title: str
    content: str
    url: str
    user_id: int
    created_at: datetime
    updated_at: datetime

    def __init__(self, title, url, content, user_id, id=None):
        super().__init__(id)
        self.title = title
        self.content = content
        self.url = url
        self.user_id = user_id

    def __repr__(self):
        return (
            f"Post(id={self.id}, title={self.title}, "
            f"content={self.content}, user_id={self.user_id})"
        )
