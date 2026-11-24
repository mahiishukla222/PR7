"""Date and time utilities using datetime and time standard modules."""
from datetime import datetime, date
import time


def current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def date_difference(first, second):
    a = datetime.strptime(first, "%Y-%m-%d").date()
    b = datetime.strptime(second, "%Y-%m-%d").date()
    return abs((b - a).days)


def format_date(value, fmt):
    return datetime.strptime(value, "%Y-%m-%d").strftime(fmt)


def stopwatch():
    # The caller waits for Enter before invoking this function; measure a short
    # interval interactively here so elapsed time is meaningful.
    start = time.perf_counter()
    input("Stopwatch started. Press Enter to stop...")
    elapsed = time.perf_counter() - start
    return f"{elapsed:.2f} seconds"


def countdown(seconds):
    print("Countdown started...")
    end = time.monotonic() + seconds
    while True:
        remaining = max(0, int(end - time.monotonic() + 0.999))
        print(f"\rTime remaining: {remaining:>4} seconds", end="", flush=True)
        if remaining <= 0: break
        time.sleep(min(1, max(0, end - time.monotonic())))
    print("\nTime's up!")


if __name__ == "__main__":
    print("Current Date and Time:", current_datetime())
