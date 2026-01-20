import pytest
from pydantic import TypeAdapter
from pydantic import ValidationError


def test_command():
    from play_launcher_sdk.types import Command

    command_adapter = TypeAdapter(Command)

    command_adapter.validate_strings('arg1 "arg two" arg3')

    with pytest.raises(ValidationError):
        command_adapter.validate_strings('arg1 arg2 "unclosed quote')


def test_date():
    from play_launcher_sdk.types import Date

    date_adapter = TypeAdapter(Date)

    date_adapter.validate_strings("12/31")

    with pytest.raises(ValidationError):
        date_adapter.validate_strings("31/12")


def test_absolute_path():
    from play_launcher_sdk.types import AbsolutePath

    absolute_path_adapter = TypeAdapter(AbsolutePath)

    absolute_path_adapter.validate_strings("C:\\absolute\\path\\to\\file.exe")
    absolute_path_adapter.validate_python(AbsolutePath("D:\\another\\absolute\\path"))

    with pytest.raises(ValidationError):
        absolute_path_adapter.validate_strings("relative\\path\\to\\file.exe")
    with pytest.raises(ValidationError):
        absolute_path_adapter.validate_python(AbsolutePath("relative\\path"))


def test_relative_path():
    from play_launcher_sdk.types import RelativePath

    relative_path_adapter = TypeAdapter(RelativePath)

    relative_path_adapter.validate_strings("relative\\path\\to\\file.exe")
    relative_path_adapter.validate_python(RelativePath("another\\relative\\path"))

    with pytest.raises(ValidationError):
        relative_path_adapter.validate_strings("C:\\absolute\\path\\to\\file.exe")
    with pytest.raises(ValidationError):
        relative_path_adapter.validate_python(RelativePath("D:\\absolute\\path"))


def test_expandable_path():
    from play_launcher_sdk.types import ExpandablePath

    expandable_path_adapter = TypeAdapter(ExpandablePath)

    expandable_path_adapter.validate_strings("%USERPROFILE%\\path\\to\\file.exe")
    expandable_path_adapter.validate_python(ExpandablePath("%APPDATA%\\another\\path"))

    with pytest.raises(ValidationError):
        expandable_path_adapter.validate_strings("C:\\absolute\\path\\to\\file.exe")
    with pytest.raises(ValidationError):
        expandable_path_adapter.validate_python(ExpandablePath("relative\\path"))
    with pytest.raises(ValidationError):
        expandable_path_adapter.validate_python(ExpandablePath("absolute\\%PATH%\\file.exe"))


def test_relative_exe_path():
    from play_launcher_sdk.types import RelativeExePath

    relative_exe_path_adapter = TypeAdapter(RelativeExePath)

    relative_exe_path_adapter.validate_strings("relative\\path\\to\\file.exe")
    relative_exe_path_adapter.validate_python(RelativeExePath("another\\relative\\path\\file.exe"))

    with pytest.raises(ValidationError):
        relative_exe_path_adapter.validate_strings("C:\\absolute\\path\\to\\file.exe")
    with pytest.raises(ValidationError):
        relative_exe_path_adapter.validate_strings("relative\\path\\to\\file.txt")
    with pytest.raises(ValidationError):
        relative_exe_path_adapter.validate_python(RelativeExePath("D:\\absolute\\path\\file.exe"))
    with pytest.raises(ValidationError):
        relative_exe_path_adapter.validate_python(RelativeExePath("relative\\path\\file.txt"))


def test_relative_json_path():
    from play_launcher_sdk.types import RelativeJsonPath

    relative_json_path_adapter = TypeAdapter(RelativeJsonPath)

    relative_json_path_adapter.validate_strings("relative\\path\\to\\file.json")
    relative_json_path_adapter.validate_python(RelativeJsonPath("another\\relative\\path\\file.json"))

    with pytest.raises(ValidationError):
        relative_json_path_adapter.validate_strings("C:\\absolute\\path\\to\\file.json")
    with pytest.raises(ValidationError):
        relative_json_path_adapter.validate_strings("relative\\path\\to\\file.txt")
    with pytest.raises(ValidationError):
        relative_json_path_adapter.validate_python(RelativeJsonPath("D:\\absolute\\path\\file.json"))
    with pytest.raises(ValidationError):
        relative_json_path_adapter.validate_python(RelativeJsonPath("relative\\path\\file.txt"))


def test_relative_txt_path():
    from play_launcher_sdk.types import RelativeTxtPath

    relative_txt_path_adapter = TypeAdapter(RelativeTxtPath)

    relative_txt_path_adapter.validate_strings("relative\\path\\to\\file.txt")
    relative_txt_path_adapter.validate_python(RelativeTxtPath("another\\relative\\path\\file.txt"))

    with pytest.raises(ValidationError):
        relative_txt_path_adapter.validate_strings("C:\\absolute\\path\\to\\file.txt")
    with pytest.raises(ValidationError):
        relative_txt_path_adapter.validate_strings("relative\\path\\to\\file.json")
    with pytest.raises(ValidationError):
        relative_txt_path_adapter.validate_python(RelativeTxtPath("D:\\absolute\\path\\file.txt"))
    with pytest.raises(ValidationError):
        relative_txt_path_adapter.validate_python(RelativeTxtPath("relative\\path\\file.json"))


def test_file_name():
    from play_launcher_sdk.types import FileName

    file_name_adapter = TypeAdapter(FileName)

    file_name_adapter.validate_strings("file.exe")
    file_name_adapter.validate_python(FileName("document.txt"))

    with pytest.raises(ValidationError):
        file_name_adapter.validate_strings("path\\to\\file.exe")
    with pytest.raises(ValidationError):
        file_name_adapter.validate_python(FileName("folder\\document.txt"))


def test_exe_file_name():
    from play_launcher_sdk.types import ExeFileName

    exe_file_name_adapter = TypeAdapter(ExeFileName)

    exe_file_name_adapter.validate_strings("file.exe")
    exe_file_name_adapter.validate_python(ExeFileName("program.exe"))

    with pytest.raises(ValidationError):
        exe_file_name_adapter.validate_strings("file.txt")
    with pytest.raises(ValidationError):
        exe_file_name_adapter.validate_strings("path\\to\\file.exe")
    with pytest.raises(ValidationError):
        exe_file_name_adapter.validate_python(ExeFileName("document.txt"))
    with pytest.raises(ValidationError):
        exe_file_name_adapter.validate_python(ExeFileName("folder\\program.exe"))


def test_png_url():
    from play_launcher_sdk.types import PngUrl

    png_url_adapter = TypeAdapter(PngUrl)

    png_url_adapter.validate_strings("https://example.com/image.png")
    png_url_adapter.validate_python(PngUrl("https://example.com/assets/picture.png"))

    with pytest.raises(ValidationError):
        png_url_adapter.validate_strings("https://example.com/image.jpg")
    with pytest.raises(ValidationError):
        png_url_adapter.validate_python(PngUrl("https://example.com/assets/photo.jpg"))


def test_webm_url():
    from play_launcher_sdk.types import WebmUrl

    webm_url_adapter = TypeAdapter(WebmUrl)

    webm_url_adapter.validate_strings("https://example.com/video.webm")
    webm_url_adapter.validate_python(WebmUrl("https://example.com/assets/movie.webm"))

    with pytest.raises(ValidationError):
        webm_url_adapter.validate_strings("https://example.com/video.mp4")
    with pytest.raises(ValidationError):
        webm_url_adapter.validate_python(WebmUrl("https://example.com/assets/clip.mp4"))


def test_icon_url():
    from play_launcher_sdk.types import IconUrl

    icon_url_adapter = TypeAdapter(IconUrl)

    icon_url_adapter.validate_strings("https://example.com/icon.ico")
    icon_url_adapter.validate_python(IconUrl("https://example.com/assets/logo.png"))

    with pytest.raises(ValidationError):
        icon_url_adapter.validate_strings("https://example.com/icon.jpg")
    with pytest.raises(ValidationError):
        icon_url_adapter.validate_python(IconUrl("https://example.com/assets/logo.gif"))


def test_image_url():
    from play_launcher_sdk.types import ImageUrl

    image_url_adapter = TypeAdapter(ImageUrl)

    image_url_adapter.validate_strings("https://example.com/image.png")
    image_url_adapter.validate_python(ImageUrl("https://example.com/another_image.jpg"))
    image_url_adapter.validate_python(ImageUrl("https://example.com/yet_another_image.webp"))

    with pytest.raises(ValidationError):
        image_url_adapter.validate_strings("https://example.com/image.gif")
    with pytest.raises(ValidationError):
        image_url_adapter.validate_python(ImageUrl("https://example.com/another_image.bmp"))


def test_zip_url():
    from play_launcher_sdk.types import ZipUrl

    zip_url_adapter = TypeAdapter(ZipUrl)

    zip_url_adapter.validate_strings("https://example.com/archive.zip")
    zip_url_adapter.validate_python(ZipUrl("https://example.com/files/data.zip"))

    with pytest.raises(ValidationError):
        zip_url_adapter.validate_strings("https://example.com/archive.7z")
    with pytest.raises(ValidationError):
        zip_url_adapter.validate_python(ZipUrl("https://example.com/files/data.rar"))


def test_archive_url():
    from play_launcher_sdk.types import ArchiveUrl

    archive_url_adapter = TypeAdapter(ArchiveUrl)

    archive_url_adapter.validate_strings("https://example.com/archive.7z")
    archive_url_adapter.validate_python(ArchiveUrl("https://example.com/files/data.zip"))

    with pytest.raises(ValidationError):
        archive_url_adapter.validate_strings("https://example.com/archive.rar")
    with pytest.raises(ValidationError):
        archive_url_adapter.validate_python(ArchiveUrl("https://example.com/files/data.tar"))


def test_split_archive_url():
    from play_launcher_sdk.types import SplitArchiveUrl

    split_archive_url_adapter = TypeAdapter(SplitArchiveUrl)

    split_archive_url_adapter.validate_strings("https://example.com/archive.zip.001")
    split_archive_url_adapter.validate_python(SplitArchiveUrl("https://example.com/files/data.7z.002"))
    split_archive_url_adapter.validate_strings("https://example.com/archive.7z")
    split_archive_url_adapter.validate_python(SplitArchiveUrl("https://example.com/files/data.zip"))

    with pytest.raises(ValidationError):
        split_archive_url_adapter.validate_strings("https://example.com/archive.rar.001")
    with pytest.raises(ValidationError):
        split_archive_url_adapter.validate_python(SplitArchiveUrl("https://example.com/files/data.tar.002"))


def test_hex_md5():
    from play_launcher_sdk.types import HexMd5

    hex_md5_adapter = TypeAdapter(HexMd5)

    hex_md5_adapter.validate_strings("d41d8cd98f00b204e9800998ecf8427e")
    hex_md5_adapter.validate_python(HexMd5(b"d41d8cd98f00b204e9800998ecf8427e"))

    with pytest.raises(ValidationError):
        hex_md5_adapter.validate_strings("d41d8cd98f00b204e9800998ecf8427")
    with pytest.raises(ValidationError):
        hex_md5_adapter.validate_strings("d41d8cd98f00b204e9800998ecf8427ee")
    with pytest.raises(ValidationError):
        hex_md5_adapter.validate_python(b"\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B")
    with pytest.raises(ValidationError):
        hex_md5_adapter.validate_python(b"\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~~")


def test_metadata_version():
    from play_launcher_sdk.types import MetadataVersion

    metadata_version_adapter = TypeAdapter(MetadataVersion)

    metadata_version_adapter.validate_strings("1.0.0.12345")
    metadata_version_adapter.validate_strings("1.2.3.4")

    with pytest.raises(ValidationError):
        metadata_version_adapter.validate_strings("1.0.0")
    with pytest.raises(ValidationError):
        metadata_version_adapter.validate_strings("1.0.0.")
