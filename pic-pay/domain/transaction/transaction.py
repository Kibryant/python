from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    id: str
    payer_id: str
    payee_id: str
    value: float
    created_at: datetime
