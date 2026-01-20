from itertools import chain

import pytest


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--all", action="store_true", help="run all combinations")


def pytest_generate_tests(metafunc: pytest.Metafunc):
    from play_launcher_sdk import ChinaId
    from play_launcher_sdk import GlobalId

    if "id" in metafunc.fixturenames:
        id = chain(GlobalId, ChinaId) if metafunc.config.getoption("--all") else (GlobalId.OFFICIAL,)
        metafunc.parametrize("id", id, scope="module")
