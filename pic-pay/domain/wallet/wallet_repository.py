from abc import ABC, abstractmethod
from .wallet import Wallet

class WalletRepository(ABC):
    @abstractmethod
    def create(self, wallet: Wallet) -> Wallet:
        pass
    
    @abstractmethod
    def update(self, wallet: Wallet) -> Wallet:
        pass
    
    @abstractmethod
    def find_by_id(self, wallet_id: str) -> Wallet:
        pass
    
    @abstractmethod
    def find_by_cpf(self, cpf: str) -> Wallet:
        pass
    
    @abstractmethod
    def find_by_email(self, email: str) -> Wallet:
        pass
    
    @abstractmethod
    def find_by_phone(self, phone: str) -> Wallet:
        pass

