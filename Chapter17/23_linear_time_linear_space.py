def f(A):
  A, max_eq_dim, irow, icol = A or [[]], 0, 0, 0
  if not A or not A[0]: return []
  B, has_value = get_B(A)
  if not has_value: return []

  for i in range(len(A)):
    for j in range(len(A)):
      left, up = B[i][j]
      imax_eq_dim = min(left, up)
      if not imax_eq_dim: continue
      down  = B[i + imax_eq_dim - 1][j][1]
      right = B[i][j + imax_eq_dim - 1][0]
      imax_eq_dim = min(imax_eq_dim, down, right)
      if imax_eq_dim <= max_eq_dim: continue
      max_eq_dim, irow, icol = imax_eq_dim, i, j

  return ([row[icol : icol + max_eq_dim]
    for row in A[irow : irow + max_eq_dim]]
    if max_eq_dim else [])

def get_B(A, value=0):
  n = len(A)
  B = [[None] * n for _ in range(n)]
  has_value = False
  for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
      if A[i][j] != value:
        B[i][j] = [0, 0]
        continue
      B[i][j] = [
          1 + (B[i+1][j][0] if i+1 < n else 0),
          1 + (B[i][j+1][1] if j+1 < n else 0),]
      has_value = True

  return (B, has_value)

assert f([[]]) == []
assert f([]) == []
assert f(None) == []

assert f([[1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],]) == []

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
assert f([[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,1],]) == [[0,0,0],
                           [0,0,0],
                           [0,0,0],]
assert f([[1,0,0,0],
          [0,1,0,0],
          [0,0,0,0],
          [0,0,0,0],]) == [[0, 0],
                           [0, 0],]
