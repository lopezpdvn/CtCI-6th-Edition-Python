def f(A):
  if not A: return None
  n = len(A)
  for k in range(n, 0, -1):
    subm = get_subm(A, k)
    if subm:
      row, col, size = subm
      return [A[i][col:col+size]
              for i in range(row, row + size)]
  return None

def get_subm(A, n):
  nsubms = len(A) - n + 1
  for i in range(nsubms):
    for j in range(nsubms):
      if is_border(A, 0, i, j, n):
        return (i, j, n)
  return None

def is_border(A, value, row, col, size):
  for k in range(size):
    if (   A[row    ][col + k] != value
      or A[row + size - 1][col + k] != value
      or A[row + k][col    ] != value
      or A[row + k][col + size - 1] != value):
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
