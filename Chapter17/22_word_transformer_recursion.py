# N is number of WW
# L is length of word
# M is the cardinality of the character set

def f(A, B, WW):
  A, B, WW = A or '', B or '', WW or ()
  from collections import deque
  has_AB, G, path, visited = (
    *build_graph(WW, A, B), deque(), set())
  if not has_AB: return ()
  return (*g(B, G, path, visited, A),)

def g(B, G, path, visited, A):
  visited.add(A)
  if A == B:
    path.appendleft(A)
    return path

  for nbor in get_nbors(G, visited, A):
    if g(B, G, path, visited, nbor):
      path.appendleft(A)
      return path

  return path

def get_nbors(G, visited, x):
  n = len(x)
  for i in range(n):
    key = f'{x[:i]}*{x[i + 1:]}'
    for nbor in G[key]:
      if nbor not in visited:
        yield nbor


def build_graph(WW, A, B):
  seen_A, seen_B = False, False
  from collections import defaultdict
  G = defaultdict(set)
  for word in WW:
    seen_A |= word == A
    seen_B |= word == B
    for i in range(len(word)):
      key = f'{word[:i]}*{word[i + 1:]}'
      G[key].add(word)

  return (seen_A and seen_B, G)

assert f('DAMP', 'DAMP', ()) == ()
assert f('DAMP', 'DAMP', ('DAMP',)) == ('DAMP',)
assert f('DAMP', 'LIKE', (
  'LIMP', 'LAMP', 'DAMP', 'LIKE', 'LIME')) == (
    'DAMP', 'LAMP', 'LIMP', 'LIME', 'LIKE')
assert f('DAMP', 'LIKE', (
  'DMMP', 'LAMP', 'LIMP', 'LIME', 'LIKE')) == ()

# Time: NL + (M^L)ML
#       where NL >= M^L
# Space: (M^L)ML
