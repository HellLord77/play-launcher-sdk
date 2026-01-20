from enum import StrEnum


class Path(StrEnum):
    GAME_CONFIGS = "/hyp/hyp-connect/api/getGameConfigs"
    GAME_CHANNEL_SDKS = "/hyp/hyp-connect/api/getGameChannelSDKs"
    GAME_DEPRECATED_FILE_CONFIGS = "/hyp/hyp-connect/api/getGameDeprecatedFileConfigs"
    GAME_BRANCHES = "/hyp/hyp-connect/api/getGameBranches"
    GAME_PACKAGES = "/hyp/hyp-connect/api/getGamePackages"
    WPF_PACKAGES = "/hyp/hyp-connect/api/getWPFPackages"
    GAME_PLUGINS = "/hyp/hyp-connect/api/getGamePlugins"
    GAMES = "/hyp/hyp-connect/api/getGames"
    GAME_SCAN_INFO = "/hyp/hyp-connect/api/getGameScanInfo"
    GAME_CONTENT = "/hyp/hyp-connect/api/getGameContent"
    ALL_GAME_BASIC_INFO = "/hyp/hyp-connect/api/getAllGameBasicInfo"
    NOTIFICATION = "/hyp/hyp-connect/api/getNotification"
