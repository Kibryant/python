def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


if __name__ == "__main__":
    array = [12, 11, 14, 5, 6, 7, 8, 1, 2, 10]

    print("Given array is", end="\n")
    print(array)

    sorted_array = merge_sort(array)
    print("Sorted array is: ", end="\n")
    print(sorted_array)
