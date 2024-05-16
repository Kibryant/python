from datetime import datetime
from domain import Wallet, Transaction, TransactionService
from wallet_repository_mock import WalletRepositoryMock
from transaction_repository_mock import TransactionRepositoryMock


def main():
    wallet_repository = WalletRepositoryMock()
    transaction_repository = TransactionRepositoryMock()

    transaction_service = TransactionService(
        transaction_repository=transaction_repository,
        wallet_repository=wallet_repository
    )

    arthur_wallet = Wallet(
        id='1',
        full_name='Arthur',
        cpf='12345678901',
        email="arthur@gmail.com",
        phone='12345678901',
        balance=1000.0,
        password='123456',
        created_at=datetime.now()
    )

    luana_wallet = Wallet(
        id='2',
        full_name='Luana',
        cpf='12345678902',
        email="luana@gmail.com",
        phone='12345678902',
        balance=1000.0,
        password='123456',
        created_at=datetime.now()
    )

    transaction = Transaction(
        id='1',
        payee_id=arthur_wallet.id,
        payer_id=luana_wallet.id,
        value=100.0,
        created_at=datetime.now()
    )

    wallet_repository.create(wallet=luana_wallet)
    wallet_repository.create(wallet=arthur_wallet)

    transaction_service.create(transaction=transaction)

    arthur = wallet_repository.find_by_id('1')
    luana = wallet_repository.find_by_id('2')

    print(arthur)
    print(luana)


if __name__ == '__main__':
    main()
