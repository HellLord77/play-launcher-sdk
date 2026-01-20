from datetime import datetime
from typing import Literal

from play_launcher_sdk.enums.notification_type import NotificationType

from .base import Base
from .message_info import MessageInfo
from .red_dot_info import RedDotInfo


class GameNotification(Base):
    notification_id: str
    type: NotificationType
    start_time: datetime
    end_time: datetime
    red_dot_info: RedDotInfo | None
    message_info: MessageInfo | None
    status: Literal["NOTIFICATION_STATUS_EFFECTIVE"]
