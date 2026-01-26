from logging_utility.logger import Logger
from logging_utility.log_type import LogType


def test_log_returns_json():
    logger = Logger("test")

    result = logger.log(LogType.INFO, "hello")

    assert isinstance(result, dict)
    assert result["message"] == "hello"
    assert result["log_type"] == "INFO"


def test_log_file_is_created(tmp_path):
    import os
    os.chdir(tmp_path)

    logger = Logger("test")
    logger.log(LogType.INFO, "hello")

    log_file = tmp_path / "test.log"

    assert log_file.exists()


def test_log_contains_metadata():
    logger = Logger("test")

    result = logger.log(LogType.INFO, "hello")

    assert "timestamp" in result
    assert "file_name" in result
    assert "function_name" in result
    assert "line_number" in result
