def count_nums_with_sqrt_close_to(n, x) -> int:
    count = 0
    for i in range(1, n+1):
        if abs(i**0.5 - x) < 0.1:
            count += 1
    return count


def main() -> None:
    print(count_nums_with_sqrt_close_to(100, 10))


if __name__ == '__main__':
    main()
