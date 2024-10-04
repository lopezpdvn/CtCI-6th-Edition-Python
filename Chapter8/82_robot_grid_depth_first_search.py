from collections import deque

def g(A, i, j):
    m, n = len(A), len(A[0])
    if i == m or j == n or not A[i][j]:
        return deque()

    if i == m - 1 and j == n - 1:
        return deque(((i, j),))

    path = g(A, i + 1, j)
    if path:
        path.appendleft((i, j))
        return path

    path = g(A, i, j + 1)
    if path:
        path.appendleft((i, j))
        return path

f = lambda maze: (*g(maze, 0, 0),)

# Time: 2^(m+n)
# Space: m + n

x = ((1, 1, 1, 1),
     (1, 1, 1, 1),
     (1, 1, 1, 1),
     (1, 1, 1, 1),)
assert f(x) == ((0, 0), (1, 0), (2, 0), (3, 0),
                (3, 1), (3, 2), (3, 3))

x = ((1, 0, 0, 0),
     (1, 1, 0, 0),
     (0, 1, 0, 0),
     (0, 1, 1, 1),)
assert f(x) == ((0, 0), (1, 0), (1, 1), (2, 1),
                (3, 1), (3, 2), (3, 3))

x = ((0, 0, 0, 0),
     (1, 1, 0, 0),
     (0, 1, 0, 0),
     (0, 1, 1, 1),)
assert f(x) == ()
