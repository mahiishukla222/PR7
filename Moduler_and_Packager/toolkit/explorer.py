"""Dynamically inspect built-in and custom Python modules using dir()."""
import importlib

ALLOWED_MODULES = {"math", "random", "datetime", "time", "uuid", "toolkit.math_utils",
                   "toolkit.random_utils", "toolkit.datetime_utils", "toolkit.uuid_utils",
                   "toolkit.file_utils"}


def explore(module_name):
    if module_name not in ALLOWED_MODULES:
        raise ValueError("Module not in allowed list. Try math, random, datetime, time, uuid, or toolkit.math_utils.")
    module = importlib.import_module(module_name)
    return sorted(name for name in dir(module) if not name.startswith("__"))


if __name__ == "__main__":
    print(explore("math"))
