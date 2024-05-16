from typing import Callable


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def apply_operation(
    operation: Callable[[int, int], int],
    a: int,
    b: int
) -> int:
    return operation(a, b)


result = apply_operation(add, 5, 3)
print(result)  # Output: 8

result = apply_operation(subtract, 10, 7)
print(result)  # Output: 3

result = apply_operation(multiply, 4, 6)
print(result)  # Output: 24
