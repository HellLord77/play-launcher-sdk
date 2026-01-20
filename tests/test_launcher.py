import pytest

pytestmark = [pytest.mark.vcr]


@pytest.fixture(scope="module")
def launcher(id):
    from play_launcher_sdk import Launcher

    return Launcher(id)


def test_game_configs(launcher):
    from play_launcher_sdk.models import GameConfigs

    game_configs = launcher.get_game_configs()
    assert isinstance(game_configs, GameConfigs)


def test_game_channel_sdks(launcher):
    from play_launcher_sdk.models import GameChannelSdks

    game_channel_sdks = launcher.get_game_channel_sdks()
    assert isinstance(game_channel_sdks, GameChannelSdks)


def test_game_deprecated_file_configs(launcher):
    from play_launcher_sdk.models import GameDeprecatedFileConfigs

    game_deprecated_file_configs = launcher.get_game_deprecated_file_configs()
    assert isinstance(game_deprecated_file_configs, GameDeprecatedFileConfigs)


def test_game_branches(launcher):
    from play_launcher_sdk.models import GameBranches

    game_branches = launcher.get_game_branches()
    assert isinstance(game_branches, GameBranches)


def test_game_packages(launcher):
    from play_launcher_sdk.models import GamePackages

    game_packages = launcher.get_game_packages()
    assert isinstance(game_packages, GamePackages)


def test_wpf_packages(launcher):
    from play_launcher_sdk.models import WpfPackages

    wpf_packages = launcher.get_wpf_packages()
    assert isinstance(wpf_packages, WpfPackages)


def test_game_plugins(launcher):
    from play_launcher_sdk.models import GamePlugins

    game_plugins = launcher.get_game_plugins()
    assert isinstance(game_plugins, GamePlugins)


def test_games(launcher):
    from play_launcher_sdk.models import Games

    games = launcher.get_games()
    assert isinstance(games, Games)


def test_game_scan_info(launcher):
    from play_launcher_sdk.models import GameScanInfo

    game_scan_info = launcher.get_game_scan_info()
    assert isinstance(game_scan_info, GameScanInfo)


def test_game_content(launcher):
    from play_launcher_sdk.models import GameContent

    games = launcher.get_games()

    for game in games.games:
        game_content = launcher.get_game_content(game)
        assert isinstance(game_content, GameContent)


def test_all_game_basic_info(launcher):
    from play_launcher_sdk.models import AllGameBasicInfo

    all_game_basic_info = launcher.get_all_game_basic_info()
    assert isinstance(all_game_basic_info, AllGameBasicInfo)


def test_notification(launcher):
    from play_launcher_sdk.models import Notification

    notification = launcher.get_notification()
    assert isinstance(notification, Notification)
