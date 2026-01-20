from pathlib import Path

import pytest


@pytest.fixture
def json_data(request: pytest.FixtureRequest, datadir: Path) -> bytes:
    path = datadir / f"{request.node.name}.json"
    return path.read_bytes()


def test_game_configs(json_data):
    from play_launcher_sdk.models import GameConfigs

    game_configs = GameConfigs.model_validate_json(json_data)
    assert isinstance(game_configs, GameConfigs)


def test_game_channel_sdks(json_data):
    from play_launcher_sdk.models import GameChannelSdks

    game_channel_sdks = GameChannelSdks.model_validate_json(json_data)
    assert isinstance(game_channel_sdks, GameChannelSdks)


def test_game_deprecated_file_configs(json_data):
    from play_launcher_sdk.models import GameDeprecatedFileConfigs

    game_deprecated_file_configs = GameDeprecatedFileConfigs.model_validate_json(json_data)
    assert isinstance(game_deprecated_file_configs, GameDeprecatedFileConfigs)


def test_game_branches(json_data):
    from play_launcher_sdk.models import GameBranches

    game_branches = GameBranches.model_validate_json(json_data)
    assert isinstance(game_branches, GameBranches)


def test_game_packages(json_data):
    from play_launcher_sdk.models import GamePackages

    game_packages = GamePackages.model_validate_json(json_data)
    assert isinstance(game_packages, GamePackages)


def test_wpf_packages(json_data):
    from play_launcher_sdk.models import WpfPackages

    wpf_packages = WpfPackages.model_validate_json(json_data)
    assert isinstance(wpf_packages, WpfPackages)


def test_game_plugins(json_data):
    from play_launcher_sdk.models import GamePlugins

    game_plugins = GamePlugins.model_validate_json(json_data)
    assert isinstance(game_plugins, GamePlugins)


def test_games(json_data):
    from play_launcher_sdk.models import Games

    games = Games.model_validate_json(json_data)
    assert isinstance(games, Games)


def test_game_scan_info(json_data):
    from play_launcher_sdk.models import GameScanInfo

    game_scan_info = GameScanInfo.model_validate_json(json_data)
    assert isinstance(game_scan_info, GameScanInfo)


def test_game_content(json_data):
    from play_launcher_sdk.models import GameContent

    game_content = GameContent.model_validate_json(json_data)
    assert isinstance(game_content, GameContent)


def test_all_game_basic_info(json_data):
    from play_launcher_sdk.models import AllGameBasicInfo

    all_game_basic_info = AllGameBasicInfo.model_validate_json(json_data)
    assert isinstance(all_game_basic_info, AllGameBasicInfo)


def test_notification(json_data):
    from play_launcher_sdk.models import Notification

    notification = Notification.model_validate_json(json_data)
    assert isinstance(notification, Notification)
