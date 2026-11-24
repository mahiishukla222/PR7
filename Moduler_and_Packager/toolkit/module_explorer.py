import importlib


def explore_module():
    name = input("\nEnter module name to explore: ")
    try:
        module = importlib.import_module(name)
        attributes = dir(module)
        print(f"\nAvailable Attributes in {name} module:")
        print(attributes[:30], "..." if len(attributes) > 30 else "")
    except ImportError:
        print("Module not found. Please enter a valid installed module name.")
