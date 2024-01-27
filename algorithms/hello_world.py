def maximum_count(mums: list[int]) -> int:
    return max(
        len([mum for mum in mums if mum < 0]),
        len([mum for mum in mums if mum > 0]),
    )


result = maximum_count([-1, -2, -3, -4, -5, -6, 7, 8, 9, 10])

print(result)
