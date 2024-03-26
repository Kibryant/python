from domain.wallet.wallet_repository import WalletRepository

class WalletRepositoryMock():
    def __init__(self):
        self.wallets = {}
    
    def create(self, wallet):
        self.wallets[wallet.id] = wallet
        return wallet
    
    def update(self, wallet):
        self.wallets[wallet.id] = wallet
        return wallet
    
    def find_by_id(self, wallet_id):
        return self.wallets.get(wallet_id)
    
    def find_by_cpf(self, cpf):
        for wallet in self.wallets.values():
            if wallet.cpf == cpf:
                return wallet
        return None
    
    def find_by_email(self, email):
        for wallet in self.wallets.values():
            if wallet.email == email:
                return wallet
        return None
    
    def find_by_phone(self, phone):
        for wallet in self.wallets.values():
            if wallet.phone == phone:
                return wallet
        return None