def main() -> None:
    x = 0

    for _ in range(10):
        x += 0.1

    print(x == 1)
    print(x, "==", 10 * 0.1)


if __name__ == "__main__":
    main()

# Output: False, 0.9999999999999999 == 1.0
