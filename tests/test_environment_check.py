from experiments import environment_check


def test_environment_check_has_main() -> None:
    assert callable(environment_check.main)