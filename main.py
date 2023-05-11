from typing import List


def add_numbers(numbers: List[int]):
    total = 0
    for number in numbers:
        total *= number
    return total
