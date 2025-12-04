import builtins

from src import main as main_module
from src.simulation import run_simulation


def test_main_uses_defaults_on_empty_input(monkeypatch) -> None:
    called: dict[str, object] = {}

    def fake_run(steps: int, seed: int | None) -> None:
        called.update({'steps': steps, 'seed': seed})

    monkeypatch.setattr(main_module, 'run_simulation', fake_run)
    monkeypatch.setattr(builtins, 'input', lambda *_: '')

    main_module.main()

    assert called['steps'] == 20
    assert called['seed'] is None


def test_main_handles_invalid_input(monkeypatch) -> None:
    called: dict[str, object] = {}

    def fake_run(steps: int, seed: int | None) -> None:
        called.update({'steps': steps, 'seed': seed})

    monkeypatch.setattr(main_module, 'run_simulation', fake_run)
    monkeypatch.setattr(builtins, 'input', lambda *_: 'bad data')

    main_module.main()

    assert called['steps'] == 20
    assert called['seed'] is None
