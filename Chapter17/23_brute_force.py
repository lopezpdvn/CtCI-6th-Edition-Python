def f(A):
  if not A: return None

  for size in range(len(A), 0, -1):
    x = get_bordered(A, size, 0)
    if x is None: continue
    row, col = x
    return [row[col : col + size]
            for row in A[row : row + size]]

  return None

def get_bordered(A, size, value):
  n_subms = len(A) - size + 1

  for i in range(n_subms):
    for j in range(n_subms):
      if is_bordered(A, i, j, size, value):
        return i, j

  return None

def is_bordered(A, i, j, size, val):
  for offset in range(size):
    if (   A[i + offset  ][j           ] != val
        or A[i + offset  ][j + size - 1] != val
        or A[i           ][j + offset  ] != val
        or A[i + size - 1][j + offset  ] != val):
      return False

  return True


assert f([[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],]) == [[0,0,0,0],
                           [0,0,0,0],
                           [0,0,0,0],
                           [0,0,0,0],]
assert f([[1,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],]) == [[0,0,0],
                           [0,0,0],
                           [0,0,0],]
assert f([[1,0,0,0],
          [0,1,0,0],
          [0,0,0,0],
          [0,0,0,0],]) == [[0, 0],
                           [0, 0],]
