from pydantic import EncoderProtocol


class HexEncoder(EncoderProtocol):
    @classmethod
    def decode(cls, data: bytes) -> bytes:
        return bytes.fromhex(data.decode())

    @classmethod
    def encode(cls, obj: bytes) -> bytes:
        return obj.hex().encode()

    @classmethod
    def get_json_format(cls) -> str:
        return "hex"
