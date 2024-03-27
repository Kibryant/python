from domain import Transaction, TransactionRepository

class TransactionRepositoryMock(TransactionRepository):
    def __init__(self):
        self.transactions = []

    def create(self, transaction: Transaction):
        self.transactions.append(transaction)
        return transaction
    
    def find_by_id(self, transaction_id: str):
        for transaction in self.transactions:
            if transaction.id == transaction_id:
                return transaction
        return None