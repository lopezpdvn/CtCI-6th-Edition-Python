def f(A):
  A = A or [[]]
  max_eq_dim = 0
  if not A or not A[0]:
    return max_eq_dim

  B = get_B(A)
  ans_e = None
  irow = None
  icol = None

  for i in range(len(A)):
    for j in range(len(A[0])):
      value, row_eq, col_eq = B[i][j]
      if value:
        continue
      imax_eq_dim = min(row_eq, col_eq)
      if imax_eq_dim <= max_eq_dim:
        continue
      max_eq_dim = imax_eq_dim
      irow = i
      icol = j

  return [row[icol : icol + max_eq_dim]
    for row in A[irow : irow + max_eq_dim]]


def get_B(A):
  m = len(A)
  n = len(A[0])
  B = [[None] * n] * m

  for i in range(m - 1, -1, -1):
    for j in range(n - 1, -1, -1):
      value = A[i][j]
      row_eq = None
      col_eq = None
      if j == n - 1 or A[i][j] != A[i][j + 1]:
        col_eq = 1
      else:
        col_eq = B[i][j + 1][2] + 1

      if i == m - 1 or A[i][j] != A[i + 1][j]:
        row_eq = 1
      else:
        row_eq = B[i + 1][j][1] + 1

      B[i][j] = (value, row_eq, col_eq)

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
