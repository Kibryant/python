def arithmetic_parenthesization(expr):
    length_of_expression = len(expr)
    print(length_of_expression)
    n = (length_of_expression + 1) // 2
    print(n)


def main():
    expr = "1+2-3+4-5"
    arithmetic_parenthesization(expr)


if __name__ == "__main__":
    main()
