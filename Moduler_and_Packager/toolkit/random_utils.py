"""Random data generation utilities."""
import random
import secrets
import string


def random_number(low, high):
    if low > high: raise ValueError("Minimum cannot be greater than maximum.")
    return random.randint(low, high)


def random_list(count, low, high):
    if count < 1 or low > high: raise ValueError("Invalid list size or range.")
    return [random.randint(low, high) for _ in range(count)]


def password(length):
    if length < 1: raise ValueError("Password length must be at least 1.")
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*?"
    return "".join(secrets.choice(alphabet) for _ in range(length))


def otp(digits=6):
    if not 4 <= digits <= 10: raise ValueError("OTP length must be between 4 and 10.")
    return "".join(secrets.choice(string.digits) for _ in range(digits))


def sample(dataset, count):
    if count > len(dataset): raise ValueError("Sample size cannot exceed dataset size.")
    return random.sample(dataset, count)


if __name__ == "__main__":
    print("Sample OTP:", otp())
