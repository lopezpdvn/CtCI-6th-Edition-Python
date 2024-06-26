# N is number of words
# L is length of word
# M is the cardinality of the character set

def f(src, dst, words):
  src, dst, words = (
    src or '', dst or '', words or ())
  if not words: return ()
  is_valid, G = build_graph(words, src, dst)
  if not is_valid: return ()
  from collections import deque
  path, visited = deque(), set()
  g(dst, G, path, visited, src)
  return (*path,)

def g(dst, G, path, visited, src):
  visited.add(src)
  if src == dst:
    path.appendleft(src)
    return True

  for nbor in get_nbors(G, visited, src):
    if g(dst, G, path, visited, nbor):
      path.appendleft(src)
      return True

  return False

def get_nbors(G, visited, x):
  n = len(x)
  for i in range(n):
    key = f'{x[:i]}*{x[i + 1:]}'
    for nbor in G[key]:
      if nbor not in visited:
        yield nbor


def build_graph(words, src, dst):
  seen_src, seen_dst = False, False
  from collections import defaultdict
  G = defaultdict(set)
  for word in words:
    seen_src |= word == src
    seen_dst |= word == dst
    for i in range(len(word)):
      key = f'{word[:i]}*{word[i + 1:]}'
      G[key].add(word)

  return (seen_src and seen_dst, G)

assert f('DAMP', 'DAMP', ()) == ()
assert f('DAMP', 'DAMP', ('DAMP',)) == ('DAMP',)
assert f('DAMP', 'LIKE', (
  'LIMP', 'LAMP', 'DAMP', 'LIKE', 'LIME')) == (
    'DAMP', 'LAMP', 'LIMP', 'LIME', 'LIKE')
assert f('DAMP', 'LIKE', (
  'DMMP', 'LAMP', 'LIMP', 'LIME', 'LIKE')) == ()

# Time: NL + (M^L)*(M-1)*L
#       where NL >= M^L
# Space: (M^L)*(M-1)*L
