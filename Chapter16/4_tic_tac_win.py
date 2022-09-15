
def f(A):
    if not A: return 0
    n = len(A)
    x = check_board(A, 0, 0, 1, 1)
    if x: return x
    x = check_board(A, 0, n - 1, 1, -1)
    if x: return x

    for i in range(n):
        x = check_board(A, i, 0, 0, 1)
        if x: return x
        x = check_board(A, 0, i, 1, 0)
        if x: return x

    return 0

def check_board(A, row, col, rowd, cold):
    n = len(A)
    could_win = 0
    for i in range(n):
        player = A[row][col]
        if not i:
            could_win = player
            row += rowd
            col += cold
            continue
        row += rowd
        col += cold
        if player != could_win: return 0

    return could_win

assert f([[1, 1],
          [2, 0]]) == 1
assert f([[1, 2, 0],
          [2, 2, 0],
          [2, 2, 1]]) == 2
