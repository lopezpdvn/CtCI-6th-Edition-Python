def f(A, x):
    if not A: return None
    m = len(A)
    if not A[0]: return None
    n = len(A[0])
    i = 0
    j = n - 1

    while i < m and j >= 0:
        if A[i][j] == x:
            return (i, j)
        if x > A[i][j]:
            i += 1
        else:
            j -= 1

    return None

assert f([[15, 20, 40, 85],
          [20, 35, 80, 95],
          [30, 55, 95, 105],
          [40, 80, 100, 120],], 55) == (2, 1)
assert f([], 12) == None
