ARRAY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(arr: list[int], target: int):
    """Binary search algorithm"""

    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    target = 10
    result = binary_search(ARRAY, target)
    print(result)


if __name__ == '__main__':
    main()
