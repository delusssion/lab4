from __future__ import annotations

from src.simulation import run_simulation


def main() -> None:
    '''
    Точка входа в приложение: запускает симуляцию казино.
    '''
    steps = 20
    seed = None

    try:
        raw_input = input(
            'Введите количество шагов и seed (опционально) через пробел '
            f'(по умолчанию {steps} шагов): '
        ).strip()
    except EOFError:
        raw_input = ''

    if raw_input:
        parts = raw_input.split()
        try:
            steps = int(parts[0])
            if len(parts) > 1:
                seed = int(parts[1])
        except ValueError:
            print('Некорректный ввод, используются значения по умолчанию.')

    run_simulation(steps=steps, seed=seed)


if __name__ == '__main__':
    main()
