from dataclasses import dataclass
from datetime import datetime
import regex as re


@dataclass
class Wallet:
    id: str
    full_name: str
    cpf: str
    email: str
    phone: str
    balance: float
    password: str
    created_at: datetime

    def __init__(
            self, 
            id: str,
            full_name: str,
            cpf: str,
            email: str,
            phone: str,
            balance: float,
            password: str,
            created_at: datetime
            ):

        self.id = id
        self.full_name = full_name
        self.cpf = cpf
        self.email = email
        self.phone = phone
        self.balance = balance
        self.password = password
        self.created_at = created_at

        if not self._is_cpf_valid():
            raise ValueError("Invalid CPF")

        if not self._is_email_valid():
            raise ValueError("Invalid email")

        if not self._is_phone_valid():
            raise ValueError("Invalid phone")

    def __str__(self) -> str:
        return f'Wallet(id={self.id}, full_name={self.full_name}, cpf={self.cpf}, email={self.email}, phone={self.phone}, balance=R${self.balance:.2f}, password={self.password}, created_at={self.created_at})'

    def debit(self, value: float):
        self.balance -= value
        return self

    def credit(self, value: float):
        self.balance += value
        return self

    def _is_cpf_valid(self):
        return len(self.cpf) == 11

    def _is_email_valid(self):
        return re.match(r"[^@]+@[^@]+\.[^@]+", self.email) is not None

    def _is_phone_valid(self):
        return re.match(r"\d{10,11}", self.phone) is not None
