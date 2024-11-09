class State:
    Empty = 0; Red = 1; Blue = 2

def f(A):
    if not A: return State.Empty
    n = len(A)
    result = evaline(A, 0, 0, 1, 1)
    if result != State.Empty: return result
    result = evaline(A, 0, n - 1, 1, -1)
    if result != State.Empty: return result
    for k in range(n):
        result = evaline(A, k, 0, 0, 1)
        if result != State.Empty: return result
        result = evaline(A, 0, k, 1, 0)
        if result != State.Empty: return result

    return State.Empty

def evaline(A, i, j, rmove, cmove):
    x, n = None, len(A)
    while i < n and j < n:
        if x is None and A[i][j] != State.Empty:
            x = A[i][j]
        elif x != A[i][j]:
            return State.Empty
        i += rmove
        j += cmove

    return x

assert f([[1, 1],
          [2, 0]]) == 1
assert f([[1, 2, 0],
          [2, 2, 0],
          [2, 2, 1]]) == 2
