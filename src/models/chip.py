from __future__ import annotations


class Chip:
    '''
    Фишка казино, поддерживает сложение для объединения ставок.
    '''

    def __init__(self, value: int) -> None:
        if value < 0:
            raise ValueError('Номинал фишки не может быть отрицательным')
        self.value = value

    def __add__(self, other: 'Chip | int') -> 'Chip':
        '''
        Объединяет фишки или добавляет числовой номинал.
        '''
        if isinstance(other, Chip):
            return Chip(self.value + other.value)
        if isinstance(other, int):
            return Chip(self.value + other)
        raise TypeError('Складывать можно только с Chip или int')

    def __repr__(self) -> str:
        return f'Chip(value={self.value})'
