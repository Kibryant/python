from datetime import datetime
from domain.wallet.wallet import Wallet


def test_wallet():
    wallet = Wallet(
        id="1",
        full_name="John Doe",
        cpf="12345678900",
        email="johndoe@gmail.com",
        phone="1234567890",
        balance=100.0,
        password="password",
        created_at=datetime.now()
    )

    assert wallet.id == "1"
    assert wallet.full_name == "John Doe"
    assert wallet.cpf == "12345678900"
    assert wallet.email == "johndoe@gmail.com"
    assert wallet.phone == "1234567890"
    assert wallet.balance == 100.0
    assert wallet.password == "password"


def test_wallet_debit():
    wallet = Wallet(
        id="1",
        full_name="John Doe",
        cpf="12345678900",
        email="johndoe@example.com",
        phone="1234567890",
        balance=100.0,
        password="password",
        created_at=datetime.now()
    )

    wallet.debit(50.0)
    assert wallet.balance == 50.0


def test_wallet_credit():
    wallet = Wallet(
        id="1",
        full_name="John Doe",
        cpf="12345678900",
        email="johndoe@example.com",
        phone="1234567890",
        balance=100.0,
        password="password",
        created_at=datetime.now()
    )

    wallet.credit(50.0)
    assert wallet.balance == 150.0


# def test_wallet_str():
#     wallet = Wallet(
#         id="1",
#         full_name="John Doe",
#         cpf="12345678900",
#         email="johndoe@example.com",
#         phone="73998437308",
#         balance=100.0,
#         password="password",
#         created_at=datetime.now()
#     )

#     expected_str = "Wallet(id='1', full_name='John Doe', cpf='123.456.789-00'," \
#                    "email='johndoe@example.com', phone='(73) 99843-7308', " \
#                    "balance=100.0, password='password', " \
#                    "created_at=<current_datetime>)"

#     assert str(wallet) == expected_str