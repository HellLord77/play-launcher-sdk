from datetime import date
from datetime import datetime
from pathlib import Path
from pathlib import PureWindowsPath
from re import fullmatch
from shlex import split
from typing import Annotated  # noqa: TID251

from annotated_types import Not
from annotated_types import Predicate
from pydantic import EncodedBytes
from pydantic import Field
from pydantic import HttpUrl
from pydantic import ValidateAs
from pydantic.experimental.pipeline import validate_as
from pydantic_extra_types.semantic_version import SemanticVersion

from .hex_encoder import HexEncoder

EmptyList = Annotated[list, Field(max_length=0)]

Command = Annotated[list[str], ValidateAs(str, split)]
Date = Annotated[date, ValidateAs(str, lambda date_: datetime.strptime(date_, "%m/%d").date())]  # noqa: DTZ007

AbsolutePath = Annotated[PureWindowsPath, Predicate(PureWindowsPath.is_absolute)]
RelativePath = Annotated[PureWindowsPath, Predicate(Not(PureWindowsPath.is_absolute))]
ExpandablePath = Annotated[PureWindowsPath, Predicate(lambda path: str(path).startswith("%"))]

RelativeExePath = Annotated[RelativePath, Predicate(lambda path: path.suffix == ".exe")]
RelativeJsonPath = Annotated[RelativePath, Predicate(lambda path: path.suffix == ".json")]
RelativeTxtPath = Annotated[RelativePath, Predicate(lambda path: path.suffix == ".txt")]

FileName = Annotated[Path, Predicate(lambda path: str(path.parent) == ".")]
ExeFileName = Annotated[FileName, Predicate(lambda path: path.suffix == ".exe")]

PngUrl = Annotated[HttpUrl, Predicate(lambda url: url.path.endswith(".png"))]
WebmUrl = Annotated[HttpUrl, Predicate(lambda url: url.path.endswith(".webm"))]
IconUrl = Annotated[HttpUrl, Predicate(lambda url: url.path.endswith((".ico", ".png")))]
ImageUrl = Annotated[HttpUrl, Predicate(lambda url: url.path.endswith((".jpg", ".png", ".webp")))]

ZipUrl = Annotated[HttpUrl, Predicate(lambda url: url.path.endswith(".zip"))]
ArchiveUrl = Annotated[HttpUrl, Predicate(lambda url: url.path.endswith((".7z", ".zip")))]
SplitArchiveUrl = Annotated[
    HttpUrl, Predicate(lambda url: fullmatch(r".*\.(?:7z|zip)(?:\.0\d{2})?$", url.path) is not None)
]

HexBytes = Annotated[bytes, EncodedBytes(encoder=HexEncoder)]

HexMd5 = Annotated[HexBytes, Field(min_length=16, max_length=16)]  # MD-5

MetadataVersion = Annotated[
    SemanticVersion,
    validate_as(str).transform(lambda version: "+".join(version.rsplit(".", 1))).validate_as(SemanticVersion),
]
