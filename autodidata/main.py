def fn1(number: int) -> int:
    """
    Returns the square of the given number.
    Args:
        number (int): The number to be squared.
    Returns:
        int: The square of the number.
    """
    return number**2


def fn2(string: str) -> str:
    """
    Returns the uppercase version of the given string.
    Args:
        string (str): The string to be converted to uppercase.
    Returns:
        str: The uppercase version of the string.
    """
    return string.upper()


def fn3(param1, param2, param3, param4=0, param5=0):
    """
    A sample function that takes multiple parameters.
    Args:
        param1: The first parameter.
        param2: The second parameter.
        param3: The third parameter.
        param4: The fourth parameter (default is 0).
        param5: The fifth parameter (default is 0).
    Returns:
        tuple: A tuple containing all parameters.
    """
    return (param1, param2, param3, param4, param5)


def fn4(number: int) -> int:
    """
    Returns the half of the given number.
    Args:
        number (int): The number to be halved.
    Returns:
        int: The half of the number.
    """
    return number // 2


def fn5(number: int) -> int:
    """
    Returns the square of the given number.
    Args:
        number (int): The number to be squared.
    Returns:
        int: The square of the number.
    """
    return number * 4


def fn6(string: str) -> float:
    try:
        return float(string)
    except ValueError:
        print("Invalid input, returning 0.0")
        return 0.0


print(fn1(4))
fn2("Hello, World!")
print(fn3(1, 2, 3))
result_fn4 = fn4(10)
print(result_fn4)
print(fn5(result_fn4))
print(fn6("3.14"))
