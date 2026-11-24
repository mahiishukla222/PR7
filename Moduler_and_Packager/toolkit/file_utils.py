"""Safe text-file operations for the project data directory."""
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _path(filename):
    name = Path(filename)
    if not filename or name.name != filename or filename in {".", ".."}:
        raise ValueError("Please enter a simple file name (without folder paths).")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return DATA_DIR / filename


def create_file(filename):
    path = _path(filename)
    path.touch(exist_ok=True)
    return f"File ready: {path.name}"


def write_file(filename, content):
    _path(filename).write_text(content, encoding="utf-8")
    return "Data written successfully!"


def read_file(filename):
    path = _path(filename)
    if not path.exists(): raise FileNotFoundError(f"'{filename}' does not exist in data/.")
    return path.read_text(encoding="utf-8")


def append_file(filename, content):
    with _path(filename).open("a", encoding="utf-8") as file:
        file.write(content + "\n")
    return "Data appended successfully!"


if __name__ == "__main__":
    print("Data folder:", DATA_DIR)
