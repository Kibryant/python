import collections


# Time complexity O(n^2)
def delete_nth_naive(array, n):
    ans = []
    for num in array:
        if ans.count(num) < n:
            ans.append(num)
    return ans


# Time Complexity O(n), using hash tables.
def delete_nth(array, n):
    result = []
    counts = collections.defaultdict(int)  # keep track of occurrences
    test = collections.defaultdict(int)  # keep track of occurrences

    for i in array:
        if counts[i] < n:
            result.append(i)
            counts[i] += 1

    return result

array = [1, 2, 3, 1, 2, 1, 2, 3]

print(delete_nth(array, 2))