def f(src, dst, words):
    if src == dst:
        return (src,)
    nbor1chr = get_nbor1chr(words)
    from collections import deque
    path = deque()
    visited = set()
    g(dst, nbor1chr, path, visited, src)
    return (*path,)

def g(dst, nbor1chr, path, visited, src):
    if src == dst:
        path.appendleft(src)
        return True

    visited.add(src)

    for nbor in get_nbors(nbor1chr, visited, src):
        x = g(dst, nbor1chr, path, visited, nbor)
        if not x: continue
        path.appendleft(src)
        return True

    return False

def get_nbors(nbor1chr, visited, x):
    n = len(x)
    for i in range(n):
        key = f'{x[:i]}*{x[i + 1:]}'
        for nbor in nbor1chr[key]:
            if nbor in visited:
                continue
            yield nbor


def get_nbor1chr(words):
    from collections import defaultdict
    nbor1chr = defaultdict(set)
    n = len(words[0])
    for word in words:
        for i in range(n):
            key = f'{word[:i]}*{word[i + 1:]}'
            nbor1chr[key].add(word)

    return nbor1chr

assert f('DAMP', 'DAMP', ()) == ('DAMP',)
assert f('DAMP', 'LIKE', (
    'LIMP', 'LAMP', 'DAMP', 'LIKE', 'LIME')) == (
        'DAMP', 'LAMP', 'LIMP', 'LIME', 'LIKE')
