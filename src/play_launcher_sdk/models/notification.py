from .base import Base
from .game_notification import GameNotification


class Notification(Base):
    notifications: list[GameNotification]
