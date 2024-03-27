from dataclasses import dataclass
from datetime import datetime
from shared import format_phone, format_cpf

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

    def __init__(self, id: str, full_name: str, cpf: str, email: str, phone: str, balance: float, password: str, created_at: datetime):
        self.id = id
        self.full_name = full_name
        self.cpf = format_cpf(cpf)
        self.email = email
        self.phone = format_phone(phone)
        self.balance = balance
        self.password = password
        self.created_at = created_at

    def __str__(self) -> str:
        return f'Wallet(id={self.id}, full_name={self.full_name}, cpf={self.cpf}, email={self.email}, phone={self.phone}, balance=R${self.balance:.2f}, password={self.password}, created_at={self.created_at})'

    def debit(self, value: float):
        self.balance -= value
        return self
    
    def credit(self, value: float):
        self.balance += value
        return self