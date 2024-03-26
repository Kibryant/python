from .transaction import Transaction
from  abc import ABC, abstractmethod

class TransactionRepository(ABC):
    @abstractmethod
    def create(self, transaction: Transaction) -> Transaction:
        pass
    
    @abstractmethod
    def find_by_id(self, transaction_id: str) -> Transaction:
        pass