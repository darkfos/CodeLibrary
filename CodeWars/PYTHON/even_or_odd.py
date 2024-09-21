"""
    Create a function that takes an integer as an argument
    and returns "Even" for even numbers or "Odd" for odd numbers.
    The function should also return "Even" or "Odd" when accessing a value at an integer index.
"""


class EvenOrOdd:
    # 6 kyu

    def __getitem__(self, number: int) -> str:
        return "Even" if number % 2 == 0 else "Odd"

    def __call__(self, number: int):
        return "Even" if number % 2 == 0 else "Odd"


even_or_odd = EvenOrOdd()