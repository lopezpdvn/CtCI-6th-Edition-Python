def g(maze):
    from collections import deque
    path = deque()
    if not maze or not maze[0]:
        return path
    m = len(maze)
    n = len(maze[0])
    h(maze, path, (m - 1, n - 1), (0, 0))
    return path

def h(maze, path, target, root):
    if root[0] > target[0] or root[1] > target[1]:
        return False
    if not maze[root[0]][root[1]]:
        return False
    if target == root:
        path.appendleft(root)
        return True
    for nbori, nborj in get_nbors(maze, root):
        found_path = h(maze, path, target,
                       (nbori, nborj))
        if not found_path:
            continue
        path.appendleft(root)
        return True
    return False

def get_nbors(maze, root):
    m = len(maze)
    n = len(maze[0])
    if (    root[0] + 1 < m
        and maze[root[0] + 1][root[1]]):
        yield root[0] + 1, root[1]
    if (    root[1] + 1 < n
        and maze[root[0]][root[1] + 1]):
        yield root[0], root[1] + 1

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
