def recursive(n: int):
    print(n)
    if n == 0:
        return
    recursive(n - 1)


# Time: O(n * Target)
def subset_sum(arr: list[int], n: int, target: int) -> bool:
    if n == 0:
        return target == 0
    # flake8: noqa
    return subset_sum(arr, n - 1, target) or subset_sum(arr, n - 1, target - arr[n - 1])


def main() -> int:
    recursive(10)
    arr = [3, 34, 4, 12, 5, 2]
    target = 9
    print(subset_sum(arr, len(arr), target))

    return 0


if __name__ == "__main__":
    main()
