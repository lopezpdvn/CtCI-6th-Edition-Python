def f(A):
  A = A or [[]]
  max_eq_dim = 0
  if not A or not A[0]: return max_eq_dim
  B = get_B(A)

  for i in range(len(A)):
    for j in range(len(A[0])):
      left, up = B[i][j]
      if up != left: continue
      imax_eq_dim = up
      down = B[i + imax_eq_dim - 1][j][1]
      right = B[i][j + imax_eq_dim - 1][0]
      if (down != imax_eq_dim or
        right != imax_eq_dim or
        imax_eq_dim <= max_eq_dim):
        continue
      max_eq_dim = imax_eq_dim
      irow = i
      icol = j

  return [row[icol : icol + max_eq_dim]
    for row in A[irow : irow + max_eq_dim]]


def get_B(A, value=0):
  n = len(A)
  B = [[None for i in range(n)] for j in range(n)]

  for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
      if A[i][j] != value:
        B[i][j] = [0, 0]
        continue
      B[i][j] = [1, 1]
      if j + 1 < n:
        B[i][j][1] += B[i][j + 1][1]
      if i + 1 < n:
        B[i][j][0] += B[i + 1][j][0]

  return B

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
