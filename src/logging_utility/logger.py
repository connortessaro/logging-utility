import json
import inspect
from logging_utility.log_type import LogType
from datetime import datetime


class Logger:
    def __init__(self, name):
        self.name = name

    # TODO: add configurable output targets (e.g. file, console, or both) via an output_target parameter
    # TODO: add log rotation support (e.g. rotate when file exceeds a size threshold or on a time interval)
    # TODO: add custom formatter support so callers can supply their own serialisation logic
    # TODO: add log filtering so that only entries at or above a minimum level are written
    def log(self, log_type: LogType, message: str):
        now = datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")

        frame = inspect.currentframe()
        prev_frame = frame.f_back
        frame_info = inspect.getframeinfo(prev_frame)
        line_number = frame_info.lineno
        file_name = frame_info.filename
        function_name = frame_info.function

        log = {
            "log_type": log_type.name,
            "message": message,
            "timestamp": now,
            "file_name": file_name,
            "function_name": function_name,
            "line_number": line_number,
        }
        res: str = json.dumps(log)

        with open(f"{self.name}.log", "a") as file:
            file.write(f"{res} \n")
        return json.loads(res)
