from .wallet_repository import WalletRepository
from .wallet import Wallet

class WalletService:
    def __init__(self, wallet_repository: WalletRepository):
        self.wallet_repository = wallet_repository

    def create(self, id: str, full_name: str, cpf: str, email: str, phone: str, balance: float, password: str, created_at: str) -> Wallet:
        wallet = Wallet(
            id=id,
            full_name=full_name,
            cpf=cpf,
            email=email,
            phone=phone,
            balance=balance,
            password=password,
            created_at=created_at
        )
        
        return wallet

    def get_wallet(self, user_id: str) -> Wallet:
        return self.wallet_repository.find_by_id(user_id)