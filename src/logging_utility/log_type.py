from enum import Enum

# TODO: consider adding custom severity levels or allowing user-defined levels
class LogType(Enum):
    INFO = 10
    DEBUG = 20
    WARNING = 30
    ERROR = 35
    CRITICAL = 40
