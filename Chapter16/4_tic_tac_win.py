class CellState:
    Empty = 0
    Red = 1
    Blue = 2

def f(A):
    if not A: return CellState.Empty
    n = len(A)
    result = evaline(A, 0, 0, 1, 1)
    if result != CellState.Empty:
        return result
    result = evaline(A, 0, n - 1, 1, -1)
    if result != CellState.Empty:
        return result
    for k in range(n):
        result = evaline(A, k, 0, 0, 1)
        if result != CellState.Empty:
            return result
        result = evaline(A, 0, k, 1, 0)
        if result != CellState.Empty:
            return result

    return CellState.Empty

def evaline(A, row, col, rmove, cmove):
    n = len(A)
    result = None
    i = row
    j = col
    while i < n and j < n:
        if result is None:
            result = A[i][j]
            if result == CellState.Empty:
                return result
        elif result != A[i][j]:
            return CellState.Empty

        i += rmove
        j += cmove

    return result

assert f([[1, 1],
          [2, 0]]) == 1
assert f([[1, 2, 0],
          [2, 2, 0],
          [2, 2, 1]]) == 2
