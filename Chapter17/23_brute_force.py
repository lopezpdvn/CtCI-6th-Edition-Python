def f(A):
    if not A: return None
    n = len(A)
    for i in range(n, 0, -1):
        subm = get_subm(A, i)
        if subm: return subm
    return None

def get_subm(A, n):
    nsubms = len(A) - n + 1
    for i in range(nsubms):
        for j in range(nsubms):
            if is_border(A, 0, i, j, nsubms):
                return (i, j, n)
    return None

def is_border(A, value, row, col, nsubms):
    n = len(A) - nsubms + 1
    for k in range(n):
        if (   A[row        ][col + k] != value
            or A[row + n - 1][col + k] != value
            or A[row + k][col        ] != value
            or A[row + k][col + n - 1] != value):
            return False
    return True


assert f([[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],]) == (0, 0, 4)

assert f([[1,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],]) == (0, 1, 3)

assert f([[1,0,0,0],
          [0,1,0,0],
          [0,0,0,0],
          [0,0,0,0],]) == (0, 2, 2)
