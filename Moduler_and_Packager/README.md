# Moduler & Packager — Multi-Utility Toolkit

A menu-driven Python project demonstrating standard-library modules, custom modules, packages, `dir()`, and the `if __name__ == "__main__"` pattern.

## Requirements
- Python 3.8 or newer
- No third-party packages required

## How to run
1. Extract the project ZIP.
2. Open a terminal / Command Prompt in the `Moduler_and_Packager` folder.
3. Run:

```bash
python main.py
```

On some systems use `python3 main.py` or `py main.py`.

## Main menu
1. Date and time operations — current date/time, date difference, custom formatting, stopwatch, countdown.
2. Mathematical operations — factorial, compound interest, trigonometry, shape areas, arithmetic.
3. Random data generation — random number/list, secure password, OTP, random sample, guessing game.
4. UUID — generate a UUID version 4 identifier.
5. File operations — create, write, read, and append text files in the project's `data/` folder.
6. Module exploration — inspect available attributes using `dir()`.
7. Exit.

## Project structure

```text
Moduler_and_Packager/
├── main.py
├── README.md
├── data/                 # Text files created by File Operations
└── toolkit/
    ├── __init__.py       # Makes toolkit a Python package
    ├── datetime_utils.py
    ├── math_utils.py
    ├── random_utils.py
    ├── uuid_utils.py
    ├── file_utils.py
    └── explorer.py
```

## Concepts demonstrated
- Built-in modules: `datetime`, `time`, `math`, `random`, `uuid`, `secrets`, `string`, `pathlib`, and `importlib`.
- Custom modules grouped into a package using `toolkit/__init__.py`.
- Reusable functions imported into `main.py`.
- `dir()` for dynamic module attribute exploration.
- `if __name__ == "__main__":` guards in the main script and custom modules.
- Input validation and file path checks.

## Notes
- Passwords and OTPs use Python's `secrets` module for stronger randomness.
- The countdown is a real-time terminal countdown.
- Files are restricted to simple filenames and stored in `data/`.
- Stopwatch: select the stopwatch option, press Enter to start, then press Enter again to stop.
