def quotient_and_remainder(x, y) -> tuple[int, int]:
    """Returns the quotient and remainder of the division of x by y."""
    q = x // y
    r = x % y
    return (q, r)


def get_data(aTuple: tuple[
    tuple[int, str],
    tuple[int, str],
    tuple[int, str],
    tuple[int, str]
]) -> tuple[int, int, int]:
    """aTuple, tuple of tuples (int, string)"""
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)


def main():
    """Main function to test the functions."""
    (quot, rem) = quotient_and_remainder(4, 5) 
    myTuple = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    (min, max, unique) = get_data(myTuple)
    print(min)
    print(max)
    print(unique)
    print(quot)
    print(rem)


if __name__ == '__main__':
    main()
