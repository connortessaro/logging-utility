# Logging Utility

A minimal Python logging system built from scratch to explore how real-world logging frameworks capture execution context, structure log data, and safely persist side effects to disk.

Rather than relying on Python’s built-in logging module, this project focuses on understanding logging at a lower level: how log records are constructed, how runtime metadata is discovered, and how filesystem behavior can be tested deterministically.

---

## Why this project exists

Most developers interact with logging systems as black boxes.
This project was built to break that abstraction and understand:

* how execution context (file, function, line number) is captured at runtime
* why structured logs are preferred over plain text
* how side effects like file creation can be tested safely
* how logging responsibilities can be cleanly separated

The goal is not to replace existing logging libraries, but to understand how they work internally.

---

## Features

* Structured JSON logging (one log entry per line)
* Enum-based log levels
* Automatic runtime metadata capture:

  * source file
  * function name
  * line number
  * timestamp
* File-based persistence to `.log` files
* Fully tested with pytest
* Isolated filesystem testing using temporary directories

---

## Example Usage

```python
from logging_utility.logger import Logger
from logging_utility.log_type import LogType

logger = Logger("app")

logger.log(LogType.INFO, "Application started")
logger.log(LogType.ERROR, "Something went wrong")
```

Produces structured log entries like:

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

Each entry is written as a single JSON object per line to `app.log`, mirroring formats commonly used in production log ingestion pipelines.

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

## Architecture Overview

```
Logger
  ├── constructs structured log record
  ├── captures runtime metadata via introspection
  └── persists log entry to disk

LogType (Enum)
  └── defines severity levels
```

Responsibilities are intentionally separated to keep logging logic readable, testable, and extensible.

---

## Testing Strategy

All tests are written using **pytest** and focus on externally observable behavior rather than implementation details.

Tests verify:

* returned structured log data
* creation of `.log` files
* presence of runtime metadata
* isolation of filesystem side effects using `tmp_path`

Run tests from the project root:

```bash
pytest
```

All file operations occur in temporary directories and leave no persistent artifacts.

---

## Key Design Decisions

* Runtime metadata is captured at log-call time using Python introspection to reflect the true execution context
* Logs are written as newline-delimited JSON to support downstream parsing and filtering
* Filesystem interactions are isolated during testing to ensure deterministic behavior
* Tests assert outcomes rather than internal state to allow refactoring without breaking test coverage

---

## Non-goals

This project intentionally does not attempt to replicate the full functionality of Python’s built-in logging module.

It does not include:

* asynchronous logging
* performance optimization
* production-grade handlers or formatters

The focus is correctness, clarity, and understanding.

---

## Planned Improvements

* Log filtering and aggregation utilities
* Configurable output targets (file vs console)
* Log rotation support
* Custom formatter support
* CLI tool for querying structured log files

---

## Tech Stack

* Python
* pytest
* inspect (runtime introspection)
* pathlib (filesystem interaction)

---

## What I learned

* how logging frameworks capture execution context at runtime
* why structured logs scale better than plain-text output
* how to test side effects without touching real files
* how separation of concerns simplifies debugging and extensibility
