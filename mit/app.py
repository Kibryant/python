def is_even(i: int) -> bool:
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """

    return i % 2 == 0


def is_triangular(k: int) -> bool:
    """
    Input: k, a positive int
    Returns True if k is a triangular number, otherwise False
    """

    i = 1
    sum = 0
    while sum < k:
        sum += i
        if sum == k:
            return True
        i += 1
    return False


def cube_root(cube: int, epsilon: float) -> float:
    """
    Input: cube, an int; epsilon, a float
    Returns a float x such that x**3 is within epsilon of cube
    """

    low = 0
    high = cube
    guess = (high + low) / 2.0
    num_guesses = 0

    while abs(guess ** 3 - cube) >= epsilon:
        if guess ** 3 < cube:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0
        num_guesses += 1

    print(f'num_guesses = {num_guesses}')
    return guess


def main() -> None:
    print(cube_root(27, 0.01))
    print(is_even(3))


if __name__ == '__main__':
    tu = (1, "mit", True)
    print(tu[0])
    main()
