"""Multi-Utility Toolkit - menu-driven Python project."""
from toolkit import datetime_utils, math_utils, random_utils, uuid_utils, file_utils, explorer

WIDTH = 56


def line():
    print("=" * WIDTH)


def pause():
    input("\nPress Enter to continue...")


def get_int(prompt, minimum=None):
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Please enter a value greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_float(prompt, minimum=None):
    while True:
        try:
            value = float(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Please enter a value greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def datetime_menu():
    while True:
        line(); print("DATETIME AND TIME OPERATIONS"); line()
        print("1. Display current date and time\n2. Difference between two dates\n3. Custom date formatting\n4. Stopwatch\n5. Countdown timer\n6. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1": print("\nCurrent Date and Time:", datetime_utils.current_datetime())
            elif choice == "2":
                a = input("Enter first date (YYYY-MM-DD): ").strip()
                b = input("Enter second date (YYYY-MM-DD): ").strip()
                print("Difference:", datetime_utils.date_difference(a, b), "days")
            elif choice == "3":
                value = input("Enter date (YYYY-MM-DD): ").strip()
                fmt = input("Enter format (default: %d-%m-%Y): ").strip() or "%d-%m-%Y"
                print("Formatted date:", datetime_utils.format_date(value, fmt))
            elif choice == "4":
                input("Press Enter to start stopwatch...")
                print("Stopwatch running. Press Enter to stop.")
                print("Elapsed:", datetime_utils.stopwatch())
            elif choice == "5":
                seconds = get_int("Enter countdown seconds: ", 0)
                datetime_utils.countdown(seconds)
            elif choice == "6": return
            else: print("Invalid choice. Try again.")
        except (ValueError, OverflowError) as exc: print("Error:", exc)
        pause()


def math_menu():
    while True:
        line(); print("MATHEMATICAL OPERATIONS"); line()
        print("1. Calculate factorial\n2. Solve compound interest\n3. Trigonometric calculations\n4. Area of geometric shapes\n5. Basic arithmetic\n6. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1": print("Factorial:", math_utils.factorial(get_int("Enter a non-negative number: ", 0)))
            elif choice == "2":
                p = get_float("Enter principal amount: ", 0); r = get_float("Enter annual rate (%): ", 0)
                t = get_float("Enter time (years): ", 0); n = get_int("Compounding periods per year (e.g. 1): ", 1)
                amount, interest = math_utils.compound_interest(p, r, t, n)
                print(f"Final Amount: {amount:.2f}\nCompound Interest: {interest:.2f}")
            elif choice == "3":
                angle = get_float("Enter angle in degrees: "); result = math_utils.trigonometry(angle)
                print(f"sin({angle}) = {result['sin']:.6f}\ncos({angle}) = {result['cos']:.6f}\ntan({angle}) = {result['tan']}")
            elif choice == "4":
                print("1. Circle  2. Rectangle  3. Triangle  4. Square")
                shape = input("Choose shape: ").strip()
                if shape == "1": print(f"Area: {math_utils.circle_area(get_float('Radius: ', 0)):.2f}")
                elif shape == "2": print(f"Area: {math_utils.rectangle_area(get_float('Length: ', 0), get_float('Width: ', 0)):.2f}")
                elif shape == "3": print(f"Area: {math_utils.triangle_area(get_float('Base: ', 0), get_float('Height: ', 0)):.2f}")
                elif shape == "4": print(f"Area: {math_utils.square_area(get_float('Side: ', 0)):.2f}")
                else: print("Invalid shape.")
            elif choice == "5":
                a = get_float("First number: "); op = input("Operator (+, -, *, /, %): ").strip(); b = get_float("Second number: ")
                print("Result:", math_utils.calculate(a, op, b))
            elif choice == "6": return
            else: print("Invalid choice. Try again.")
        except (ValueError, ZeroDivisionError, OverflowError) as exc: print("Error:", exc)
        pause()


def random_menu():
    while True:
        line(); print("RANDOM DATA GENERATION"); line()
        print("1. Generate random number\n2. Generate random list\n3. Create random password\n4. Generate random OTP\n5. Random sample from dataset\n6. Simple number guessing game\n7. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1":
                low = get_int("Minimum: "); high = get_int("Maximum: ")
                print("Random Number:", random_utils.random_number(low, high))
            elif choice == "2":
                count = get_int("How many numbers? ", 1); low = get_int("Minimum: "); high = get_int("Maximum: ")
                print("Random List:", random_utils.random_list(count, low, high))
            elif choice == "3": print("Generated Password:", random_utils.password(get_int("Password length: ", 1)))
            elif choice == "4": print("Generated OTP:", random_utils.otp(get_int("OTP digits (4-10): ", 4)))
            elif choice == "5":
                values = input("Enter items separated by commas: ").split(",")
                count = get_int("Sample size: ", 1); print("Random Sample:", random_utils.sample([x.strip() for x in values if x.strip()], count))
            elif choice == "6":
                secret = random_utils.random_number(1, 20); print("Guess a number from 1 to 20. You have 5 attempts.")
                for attempt in range(5):
                    guess = get_int(f"Attempt {attempt + 1}: ")
                    if guess == secret: print("Correct! You won."); break
                    print("Too low!" if guess < secret else "Too high!")
                else: print("Game over. Number was:", secret)
            elif choice == "7": return
            else: print("Invalid choice. Try again.")
        except ValueError as exc: print("Error:", exc)
        pause()


def file_menu():
    while True:
        line(); print("FILE OPERATIONS (CUSTOM MODULE)"); line()
        print("Files are stored in the project's data/ folder.\n1. Create a new file\n2. Write to a file\n3. Read from a file\n4. Append to a file\n5. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1": print(file_utils.create_file(input("Enter file name: ").strip()))
            elif choice == "2": print(file_utils.write_file(input("Enter file name: ").strip(), input("Enter data to write: ")))
            elif choice == "3": print("\nFile Content:\n" + file_utils.read_file(input("Enter file name: ").strip()))
            elif choice == "4": print(file_utils.append_file(input("Enter file name: ").strip(), input("Enter data to append: ")))
            elif choice == "5": return
            else: print("Invalid choice. Try again.")
        except (OSError, ValueError) as exc: print("Error:", exc)
        pause()


def main():
    while True:
        line(); print("WELCOME TO MULTI-UTILITY TOOLKIT"); line()
        print("1. Datetime and Time Operations\n2. Mathematical Operations\n3. Random Data Generation\n4. Generate Unique Identifiers (UUID)\n5. File Operations (Custom Module)\n6. Explore Module Attributes (dir())\n7. Exit")
        line(); choice = input("Enter your choice: ").strip()
        if choice == "1": datetime_menu()
        elif choice == "2": math_menu()
        elif choice == "3": random_menu()
        elif choice == "4":
            print("\nGenerated UUID:", uuid_utils.generate_uuid())
            print("UUID Version 4:", uuid_utils.generate_uuid()); pause()
        elif choice == "5": file_menu()
        elif choice == "6":
            name = input("Enter module name (math, random, datetime, uuid, time): ").strip()
            try: print("\nAvailable Attributes:\n", explorer.explore(name))
            except (ImportError, ValueError) as exc: print("Error:", exc)
            pause()
        elif choice == "7":
            line(); print("Thank you for using the Multi-Utility Toolkit!"); line(); break
        else: print("Invalid choice. Please select 1-7."); pause()


if __name__ == "__main__":
    main()
