from datetime import datetime
from wallet_repository_mock import WalletRepositoryMock
from domain.wallet.wallet import Wallet


def main():
    wallet_repository = WalletRepositoryMock()

    arthur_wallet = Wallet(
        id='1',
        full_name='Arthur',
        cpf='12345678901',
        email="arthurgustavon@gmail.com",
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

    luana = wallet_repository.create(wallet=luana_wallet)
    arthur = wallet_repository.create(wallet=arthur_wallet)

    print(arthur)


if __name__ == '__main__':
    main()