# Logging Utility

A lightweight Python logging utility that generates structured JSON logs, captures runtime metadata, and persists logs to disk with full pytest coverage.

Built to explore how real-world logging systems work internally, including runtime introspection, file-based persistence, and isolated testing of side effects.

---

## Features

* Structured JSON logging (one log entry per line)
* Enum-based log levels
* Automatic runtime metadata capture:

  * source file
  * function name
  * line number
  * timestamp
* Writes logs to `.log` files on disk
* Fully tested with pytest
* Isolated filesystem testing using temporary directories

---

## Project Structure

```
logging-utility/
├── src/
│   └── logging_utility/
│       ├── __init__.py
│       ├── logger.py
│       └── log_type.py
├── tests/
│   └── logger_test.py
├── conftest.py
└── .gitignore
```

---

## Example Usage

```python
from logging_utility.logger import Logger
from logging_utility.log_type import LogType

logger = Logger("app")

logger.log(LogType.INFO, "Application started")
logger.log(LogType.ERROR, "Something went wrong")
```

Produces log entries like:

```json
{
  "log_type": "INFO",
  "message": "Application started",
  "timestamp": "2026-01-25 19:42:11",
  "file_name": "main.py",
  "function_name": "run",
  "line_number": 14
}
```

Each entry is written as a single JSON object per line in `app.log`.

---

## Why JSON Logging?

Structured logs make it easier to:

* parse programmatically
* filter by severity or metadata
* aggregate across systems
* analyze behavior after execution

This mirrors how production systems handle observability and debugging.

---

## Testing

Tests are written using **pytest** and verify:

* returned structured log data
* creation of `.log` files
* presence of runtime metadata
* isolated filesystem behavior using `tmp_path`

Run tests from the project root:

```bash
pytest
```

All filesystem interactions occur in temporary directories and leave no persistent files.

---

## Design Notes

* Logging responsibilities are cleanly separated
* Runtime metadata is captured via Python introspection
* File operations use safe context managers
* Tests validate observable behavior rather than implementation details

---

## Planned Improvements

* Log filtering and aggregation utilities
* Configurable output targets (file vs console)
* Log rotation support
* Custom formatter support
* CLI tool for querying log files

---

## Tech Stack

* Python
* pytest
* inspect (runtime introspection)
* pathlib (filesystem interaction)

---

## Motivation

This project was built to gain a deeper understanding of how logging frameworks operate under the hood, including execution-context capture, safe persistence, and testing side effects in isolation.
