from typing import Literal

from .base import Base


class ResponseBody[T: Base](Base):
    retcode: Literal[0]
    message: Literal["OK"]
    data: T
