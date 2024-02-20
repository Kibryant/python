# Bad implementation of the fibonacci sequence O(2^n)
def bad_fibonacci(n: int):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


# Good implementation of the fibonacci sequence O(n)
def fibonacci(n: int):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


memo = {}


# Good implementation of the fibonacci sequence O(n)
def fibonacci_with_memo(n: int):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_with_memo(n - 1) + fibonacci_with_memo(n - 2)
    return memo[n]


if __name__ == "__main__":
    print(fibonacci(400))
    print(fibonacci_with_memo(400))
