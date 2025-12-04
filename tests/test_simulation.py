from src.simulation import run_simulation


def test_run_simulation_deterministic_output(capsys) -> None:
    run_simulation(steps=3, seed=0)
    output = capsys.readouterr().out

    assert 'Старт симуляции' in output
    assert '-- Шаг 1 --' in output
    assert '-- Шаг 3 --' in output
