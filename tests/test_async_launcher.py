import pytest

pytestmark = [pytest.mark.anyio, pytest.mark.vcr]


@pytest.fixture(scope="module")
def launcher():
    from play_launcher_sdk import AsyncLauncher

    return AsyncLauncher()


async def test_game_configs(launcher):
    from play_launcher_sdk.models import GameConfigs

    game_configs = await launcher.get_game_configs()
    assert isinstance(game_configs, GameConfigs)


async def test_game_channel_sdks(launcher):
    from play_launcher_sdk.models import GameChannelSdks

    game_channel_sdks = await launcher.get_game_channel_sdks()
    assert isinstance(game_channel_sdks, GameChannelSdks)


async def test_game_deprecated_file_configs(launcher):
    from play_launcher_sdk.models import GameDeprecatedFileConfigs

    game_deprecated_file_configs = await launcher.get_game_deprecated_file_configs()
    assert isinstance(game_deprecated_file_configs, GameDeprecatedFileConfigs)


async def test_game_branches(launcher):
    from play_launcher_sdk.models import GameBranches

    game_branches = await launcher.get_game_branches()
    assert isinstance(game_branches, GameBranches)


async def test_game_packages(launcher):
    from play_launcher_sdk.models import GamePackages

    game_packages = await launcher.get_game_packages()
    assert isinstance(game_packages, GamePackages)


async def test_wpf_packages(launcher):
    from play_launcher_sdk.models import WpfPackages

    wpf_packages = await launcher.get_wpf_packages()
    assert isinstance(wpf_packages, WpfPackages)


async def test_game_plugins(launcher):
    from play_launcher_sdk.models import GamePlugins

    game_plugins = await launcher.get_game_plugins()
    assert isinstance(game_plugins, GamePlugins)


async def test_games(launcher):
    from play_launcher_sdk.models import Games

    games = await launcher.get_games()
    assert isinstance(games, Games)


async def test_game_scan_info(launcher):
    from play_launcher_sdk.models import GameScanInfo

    game_scan_info = await launcher.get_game_scan_info()
    assert isinstance(game_scan_info, GameScanInfo)


async def test_game_content(launcher):
    from play_launcher_sdk.models import GameContent

    games = await launcher.get_games()
    game = games.games[0]

    game_content = await launcher.get_game_content(game)
    assert isinstance(game_content, GameContent)


async def test_all_game_basic_info(launcher):
    from play_launcher_sdk.models import AllGameBasicInfo

    all_game_basic_info = await launcher.get_all_game_basic_info()
    assert isinstance(all_game_basic_info, AllGameBasicInfo)


async def test_notification(launcher):
    from play_launcher_sdk.models import Notification

    notification = await launcher.get_notification()
    assert isinstance(notification, Notification)
