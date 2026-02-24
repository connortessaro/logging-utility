# 🪵 Logging Utility

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/tested%20with-pytest-0A9EDC?logo=pytest&logoColor=white" alt="pytest">
  <img src="https://img.shields.io/badge/logs-JSON-orange" alt="JSON logs">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
</p>

<p align="center">
  A minimal Python logging system built from scratch to explore how real-world logging frameworks capture execution context, structure log data, and safely persist side effects to disk.
</p>

---

## 📋 Table of Contents

- [Why this project exists](#why-this-project-exists)
- [Features](#features)
- [Example Usage](#example-usage)
- [Project Structure](#project-structure)
- [Architecture Overview](#architecture-overview)
- [Testing Strategy](#testing-strategy)
- [Key Design Decisions](#key-design-decisions)
- [Planned Improvements](#planned-improvements)
- [Tech Stack](#tech-stack)
- [What I learned](#what-i-learned)

---

## 💡 Why this project exists

Most developers interact with logging systems as black boxes. This project was built to break that abstraction and understand:

- 🔍 how execution context (file, function, line number) is captured at runtime
- 📐 why structured logs are preferred over plain text
- 🧪 how side effects like file creation can be tested safely
- 🧩 how logging responsibilities can be cleanly separated

> The goal is not to replace existing logging libraries, but to understand how they work internally.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 Structured JSON logging | One log entry per line (newline-delimited JSON) |
| 🏷️ Enum-based log levels | Clean, type-safe severity levels via `LogType` |
| 🔎 Runtime metadata capture | Automatically records file, function, line number, and timestamp |
| 💾 File-based persistence | Writes logs to `.log` files |
| ✅ Fully tested | Pytest suite with isolated filesystem tests using `tmp_path` |

---

## 🚀 Example Usage

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

## 📁 Project Structure

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

## 🏗️ Architecture Overview

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

## 🧪 Testing Strategy

All tests are written using **pytest** and focus on externally observable behavior rather than implementation details.

Tests verify:

- ✅ returned structured log data
- ✅ creation of `.log` files
- ✅ presence of runtime metadata
- ✅ isolation of filesystem side effects using `tmp_path`

Run tests from the project root:

```bash
pytest
```

All file operations occur in temporary directories and leave no persistent artifacts.

---

## 🔑 Key Design Decisions

- **Runtime introspection** — metadata is captured at log-call time to reflect the true execution context
- **Newline-delimited JSON** — supports downstream parsing and filtering
- **Isolated filesystem tests** — deterministic behavior with no real file I/O during testing
- **Outcome-based assertions** — tests assert observable results, allowing safe internal refactoring

---

## 🗺️ Planned Improvements

- [ ] Log filtering and aggregation utilities
- [ ] Configurable output targets (file vs console)
- [ ] Log rotation support
- [ ] Custom formatter support
- [ ] CLI tool for querying structured log files

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python** | Core language |
| **pytest** | Test framework |
| **inspect** | Runtime introspection |
| **pathlib** | Filesystem interaction |

---

## 📚 What I learned

- How logging frameworks capture execution context at runtime
- Why structured logs scale better than plain-text output
- How to test side effects without touching real files
- How separation of concerns simplifies debugging and extensibility
