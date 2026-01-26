from logging_utility.logger import Logger
from logging_utility.log_type import LogType


def test_log_returns_json():
    logger = Logger("test")

    result = logger.log(log_type=LogType.INFO, message="hello")
    assert result["message"] == "hello"
    assert result["log_type"] == "INFO"
