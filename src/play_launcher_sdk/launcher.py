from http import HTTPMethod
from typing import override

from httpx import URL
from httpx import AsyncClient
from httpx import Client
from httpx import Request
from httpx import Response

from .enums.language import Language
from .enums.notification_type import NotificationType
from .enums.path import Path
from .id import GlobalId
from .id import Id
from .models import AllGameBasicInfo
from .models import GameBranches
from .models import GameChannelSdks
from .models import GameConfigs
from .models import GameContent
from .models import GameDeprecatedFileConfigs
from .models import GamePackages
from .models import GamePlugins
from .models import Games
from .models import GameScanInfo
from .models import Notification
from .models import WpfPackages
from .models.base import Base
from .models.game import Game
from .models.game_status import GameStatus
from .models.response_body import ResponseBody


def parse_json_response_as[T: Base](model_type: type[T], response: Response) -> T:
    return ResponseBody[model_type].model_validate_json(response.content).data


class Launcher:
    def __init__(self, id: Id = GlobalId.OFFICIAL, *, client: Client | None = None) -> None:
        self.id = id

        if client is None:
            client = Client()
        self.client = client

    def _get_request(
        self,
        path: Path,
        *game_ids: Game | GameStatus,
        game_id: Game | GameStatus | None,
        type_: NotificationType | None,
        language: Language | None,
    ) -> Request:
        url = URL(scheme="https", host=self.id.HOST, path=path)
        params: dict[str, str | int | list[str]] = {"launcher_id": self.id}

        if path == Path.GAME_CHANNEL_SDKS:
            params["channel"] = 1
            params["sub_channel"] = 3
        if game_ids:
            params["game_ids[]"] = [game_id.id for game_id in game_ids]
        if game_id is not None:
            params["game_id"] = game_id.id
        if type_ is not None:
            params["type"] = type_
        if language is not None:
            params["language"] = language

        return Request(HTTPMethod.GET, url, params=params)

    def _get_response(self, request: Request) -> Response:
        response = self.client.send(request)
        response.raise_for_status()
        return response

    def _get_data[T: Base](
        self,
        path: Path,
        *game_ids: Game | GameStatus,
        game_id: Game | GameStatus | None = None,
        type_: NotificationType | None = None,
        language: Language | None = None,
        data: type[T],
    ) -> T | None:
        request = self._get_request(path, *game_ids, game_id=game_id, type_=type_, language=language)
        response = self._get_response(request)

        return parse_json_response_as(data, response)

    def get_game_configs(self, *game_ids: Game | GameStatus) -> GameConfigs:
        return self._get_data(Path.GAME_CONFIGS, *game_ids, data=GameConfigs)

    def get_game_channel_sdks(self, *game_ids: Game | GameStatus) -> GameChannelSdks:
        return self._get_data(Path.GAME_CHANNEL_SDKS, *game_ids, data=GameChannelSdks)

    def get_game_deprecated_file_configs(self, *game_ids: Game | GameStatus) -> GameDeprecatedFileConfigs:
        return self._get_data(Path.GAME_DEPRECATED_FILE_CONFIGS, *game_ids, data=GameDeprecatedFileConfigs)

    def get_game_branches(self, *game_ids: Game | GameStatus) -> GameBranches:
        return self._get_data(Path.GAME_BRANCHES, *game_ids, data=GameBranches)

    def get_game_packages(self, *game_ids: Game | GameStatus) -> GamePackages:
        return self._get_data(Path.GAME_PACKAGES, *game_ids, data=GamePackages)

    def get_wpf_packages(self, *game_ids: Game | GameStatus) -> WpfPackages:
        return self._get_data(Path.WPF_PACKAGES, *game_ids, data=WpfPackages)

    def get_game_plugins(self, *game_ids: Game | GameStatus) -> GamePlugins:
        return self._get_data(Path.GAME_PLUGINS, *game_ids, data=GamePlugins)

    def get_games(self) -> Games:
        return self._get_data(Path.GAMES, data=Games)

    def get_game_scan_info(self, *game_ids: Game | GameStatus) -> GameScanInfo:
        return self._get_data(Path.GAME_SCAN_INFO, *game_ids, data=GameScanInfo)

    def get_game_content(self, game_id: Game | GameStatus, language: Language | None = None) -> GameContent:
        return self._get_data(Path.GAME_CONTENT, game_id=game_id, language=language, data=GameContent)

    def get_all_game_basic_info(self, game_id: Game | GameStatus | None = None) -> AllGameBasicInfo:
        return self._get_data(Path.ALL_GAME_BASIC_INFO, game_id=game_id, data=AllGameBasicInfo)

    def get_notification(self, type: NotificationType | None = None) -> Notification:  # noqa: A002
        return self._get_data(Path.NOTIFICATION, type_=type, data=Notification)


class AsyncLauncher(Launcher):
    @override
    def __init__(self, *, client: AsyncClient | None = None) -> None:
        if client is None:
            client = AsyncClient()

        super().__init__(client=client)

    @override
    async def _get_response(self, request: Request) -> Response:
        response = await self.client.send(request)
        response.raise_for_status()
        return response

    @override
    async def _get_data[T: Base](
        self,
        path: Path,
        *game_ids: Game | GameStatus,
        game_id: Game | GameStatus | None = None,
        type_: NotificationType | None = None,
        language: Language | None = None,
        data: type[T],
    ) -> T | None:
        request = self._get_request(path, *game_ids, game_id=game_id, type_=type_, language=language)
        response = await self._get_response(request)

        return parse_json_response_as(data, response)
