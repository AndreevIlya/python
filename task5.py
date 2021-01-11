from functools import reduce

print(
    reduce(
        lambda result, x: result * x,
        [x for x in range(100, 1001, 2)]
    )
)
