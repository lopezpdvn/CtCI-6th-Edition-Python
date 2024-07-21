def g(A):
  from collections import deque
  seq = deque()
  if (   not A or not A[0] or not A[-1][-1]
      or not h(A, seq, 0, 0)):
    return deque()
  return seq

def h(A, seq, i, j):
  if i == len(A) or j == len(A[0]) or not A[i][j]:
    return False
  if ((i == len(A) - 1 and j == len(A[0]) - 1) 
    or h(A, seq, i+1, j) or h(A, seq, i, j+1)):
    seq.appendleft((i, j))
    return True

  return False

f = lambda maze: (*g(maze),)

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
