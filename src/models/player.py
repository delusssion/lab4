from __future__ import annotations


class Player:
    '''
    Игрок казино. Хранит имя и баланс и позволяет изменять баланс контролируемо.
    '''

    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance

    def deposit(self, amount: int) -> None:
        '''
        Пополнение баланса.
        '''
        self.balance += max(0, amount)

    def withdraw(self, amount: int) -> int:
        '''
        Снятие средств; возвращает фактически снятую сумму (не меньше нуля).
        '''
        safe_amount = min(self.balance, max(0, amount))
        self.balance -= safe_amount
        return safe_amount

    def __repr__(self) -> str:
        return f'Player(name={self.name!r}, balance={self.balance})'
