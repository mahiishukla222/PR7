"""Mathematical utility functions."""
import math


def factorial(number):
    if number < 0: raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(number)


def compound_interest(principal, rate, years, periods=1):
    if periods <= 0: raise ValueError("Periods must be greater than zero.")
    amount = principal * (1 + rate / (100 * periods)) ** (periods * years)
    return amount, amount - principal


def trigonometry(degrees):
    radians = math.radians(degrees)
    sine, cosine = math.sin(radians), math.cos(radians)
    tangent = "undefined" if math.isclose(cosine, 0, abs_tol=1e-12) else math.tan(radians)
    return {"sin": sine, "cos": cosine, "tan": tangent}


def circle_area(radius): return math.pi * radius ** 2

def rectangle_area(length, width): return length * width

def triangle_area(base, height): return 0.5 * base * height

def square_area(side): return side ** 2


def calculate(a, operator, b):
    operations = {"+": lambda: a + b, "-": lambda: a - b, "*": lambda: a * b,
                  "/": lambda: a / b, "%": lambda: a % b}
    if operator not in operations: raise ValueError("Unsupported operator.")
    if operator in {"/", "%"} and b == 0: raise ZeroDivisionError("Cannot divide by zero.")
    return operations[operator]()


if __name__ == "__main__":
    print("5! =", factorial(5))
