from itertools import chain

import pytest


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--all", action="store_true", help="run all combinations")


def pytest_generate_tests(metafunc: pytest.Metafunc):
    from play_launcher_sdk import ChinaLauncherId
    from play_launcher_sdk import GlobalLauncherId

    if "id" in metafunc.fixturenames:
        id = (
            chain(GlobalLauncherId, ChinaLauncherId)
            if metafunc.config.getoption("--all")
            else (GlobalLauncherId.OFFICIAL,)
        )
        metafunc.parametrize("id", id, scope="module")
