from enum import StrEnum
from enum import nonmember
from typing import ClassVar

from .host import Host


class LauncherId(StrEnum):
    HOST: ClassVar[Host]


class GlobalLauncherId(LauncherId):
    EPIC_GOOGLE_GENSHIN_IMPACT = "8fANlj5K7I"
    EPIC_GOOGLE_HONKAI_STAR_RAIL = "gGoJxKOusQ"
    EPIC_GOOGLE_ZENLESS_ZONE_ZERO = "0hUu4SbmhI"

    EPIC_GOOGLE_HONKAI_IMPACT_3RD_ASIA = "L83o6ar17w"
    EPIC_GOOGLE_HONKAI_IMPACT_3RD_GLOBAL = "ACQazS79kX"
    EPIC_GOOGLE_HONKAI_IMPACT_3RD_JAPAN = "6runUel2hp"
    EPIC_GOOGLE_HONKAI_IMPACT_3RD_KOREA = "kkd8eq3Nnd"
    EPIC_GOOGLE_HONKAI_IMPACT_3RD_SEA = "GTLARRVLB5"

    OFFICIAL = "VYTpXlbWo8"
    HOST = nonmember(Host.GLOBAL)


class ChinaLauncherId(LauncherId):
    BILIBILI_GENSHIN_IMPACT = "umfgRO5gh5"
    BILIBILI_HONKAI_STAR_RAIL = "6P5gHMNyK3"
    BILIBILI_ZENLESS_ZONE_ZERO = "xV0f4r1GT0"

    OFFICIAL = "jGHBHlcOq1"
    HOST = nonmember(Host.CHINA)
