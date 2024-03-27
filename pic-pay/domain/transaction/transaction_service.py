from .transaction_repository import TransactionRepository
from .transaction import Transaction
from ..wallet.wallet_repository import WalletRepository

class TransactionService:
    def __init__(self, transaction_repository: TransactionRepository, wallet_repository: WalletRepository):
        self.transaction_repository = transaction_repository
        self.wallet_repository = wallet_repository

    def validate(self, transaction: Transaction):
        if transaction.value <= 0:
            raise ValueError('Transaction value must be greater than zero')

        payer_wallet = self.wallet_repository.find_by_id(transaction.payer_id)
        payee_wallet = self.wallet_repository.find_by_id(transaction.payee_id)

        if payer_wallet.balance < transaction.value:
            raise ValueError('Insufficient balance')
        
        if payer_wallet.id == payee_wallet.id:
            raise ValueError('Payer and payee wallets cannot be the same')

    def create(self, transaction: Transaction) -> Transaction:
        self.validate(transaction)

        new_transaction = self.transaction_repository.create(transaction)

        payer_wallet = self.wallet_repository.find_by_id(transaction.payer_id)
        payee_wallet = self.wallet_repository.find_by_id(transaction.payee_id)

        payer_wallet.debit(transaction.value)
        payee_wallet.credit(transaction.value)

        return new_transaction
        
