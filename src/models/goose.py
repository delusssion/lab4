from __future__ import annotations

from src.constants import MERGE_HYPE_BONUS
from src.models.player import Player


class Goose:
    '''
    Базовый гусь в казино.
    '''

    def __init__(self, name: str, honk_volume: int) -> None:
        self.name = name
        self.honk_volume = honk_volume

    def __add__(self, other: 'Goose') -> 'Goose':
        '''
        Объединение гусей в стаю: громкость усиливается, имя складывается.
        '''
        if not isinstance(other, Goose):
            raise TypeError('Можно объединять только с другим гусем')
        combined_volume = max(self.honk_volume, other.honk_volume) + MERGE_HYPE_BONUS
        return Goose(name=f'{self.name}-{other.name} Flock', honk_volume=combined_volume)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name!r}, honk_volume={self.honk_volume})'


class WarGoose(Goose):
    '''
    Боевой гусь, который атакует игроков.
    '''

    def attack(self, player: Player, damage: int) -> int:
        '''
        Атакует игрока, снижая его баланс; возвращает нанесённый урон.
        '''
        return player.withdraw(damage)


class HonkGoose(Goose):
    '''
    Гусь, влияющий на баланс игрока криком.
    '''

    def __call__(self, player: Player, impact: int) -> int:
        '''
        Особенность гуся: громкий крик заставляет игрока уронить часть фишек.
        Возвращает потерянную сумму.
        '''
        return player.withdraw(impact)
