from typing import Callable


def apply_operation(
    operation: Callable[[int, int], int],
    a: int,
    b: int
) -> int:
    """Apply the operation to the two numbers and return the result."""
    return operation(a, b)


def main():
    result = apply_operation(lambda a, b: a + b, 5, 3)
    print(result)  # Output: 8

    result = apply_operation(lambda a, b: a - b, 10, 7)
    print(result)  # Output: 3

    result = apply_operation(lambda a, b: a * b, 4, 6)
    print(result)  # Output: 24

    print((lambda a, b: a + b)(10, 10))


if __name__ == "__main__":
    main()
