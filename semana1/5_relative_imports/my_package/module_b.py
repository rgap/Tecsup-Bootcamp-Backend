# relative import
from .module_a import greet


def display_greeting():
    print(greet("Relative"))


if __name__ == "__main__":
    display_greeting()
