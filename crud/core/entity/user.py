from dataclasses import dataclass, field
from ..shared.entity import Entity
from .post import Post
from datetime import datetime


@dataclass
class User(Entity):
    name: str
    email: str
    post: list[Post] = field(default_factory=list)
    _password: str = ""
    is_active: bool = False
    is_admin: bool = False
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def __init__(self, name, email, password, is_active, is_admin, id=None):
        super().__init__(id)
        self.name = name
        self.email = email
        self._password = password
        self.is_active = is_active
        self.is_admin = is_admin

    @property
    def password(self):
        return self._password
