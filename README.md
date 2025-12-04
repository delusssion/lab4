# Лабораторная работа №4. Казино и гуси — симуляция

## Цель проекта
Учебная симуляция казино с игроками и гусями: демонстрация пользовательских коллекций, наследования, магических методов и псевдослучайной логики.

## Структура проекта
```
lab4/
├── src/
│   ├── __init__.py
│   ├── collections_ext/
│   │   ├── __init__.py
│   │   ├── casino_balance.py
│   │   ├── goose_collection.py
│   │   └── player_collection.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── chip.py
│   │   ├── goose.py
│   │   └── player.py
│   ├── __init__.py
│   ├── casino.py
│   ├── constants.py
│   ├── main.py
│   └── simulation.py
├── tests/
│   ├── __init__.py
│   ├── test_casino_balance.py
│   ├── test_casino.py
│   ├── test_chip.py
│   ├── test_goose.py
│   ├── test_main.py
│   ├── test_player.py
│   └── test_simulation.py
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml
├── README.md
├── requirements.txt
└── uv.lock
```

## Используемые технологии
- Python 3.12+.
- pytest, pytest-cov для тестирования и покрытия.

## Реализованное
- Базовый класс `Goose` и два производных (`WarGoose`, `HonkGoose`) с разным поведением.
- Пользовательские коллекции: списковые (`PlayerCollection`, `GooseCollection` срезы/индексация/итерация) и словарная (`CasinoBalance` с логированием балансов).
- Магические методы с предметным смыслом: `Goose.__add__` (объединение стаи), `HonkGoose.__call__`, `Chip.__add__`, `__contains__/__repr__` в коллекциях.
- Псевдослучайная симуляция казино с событиями (ставка, бонус, атака, крик, кража, объединение гусей, паника).
- Логи событий и изменений балансов выводятся в консоль.

## Принятые решения и допущения
- Балансы игроков и доходы гусей ведутся раздельно через `CasinoBalance`.
- При одинаковом `seed` события идентичны (используется `random.Random(seed)`).

## Тестирование
- **17 модульных тестов** с покрытием более 90% всей функциональности.
- `tests/` проверяют коллекции, модели, события казино, симуляцию, обработку ввода в `main`.
- Все тесты проходят (см. секцию запуска).

## Запуск тестов и программы
1. Создать и активировать виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate # macOS/Linux
```
ИЛИ
```
venv\Scripts\activate #Windows
```
2. Установить зависимости:
```
pip install -r requirements.txt
```
3. Запуск тестов
```
python3 -m pytest
```
4. Запуск программы
```
python -m src.main
```
