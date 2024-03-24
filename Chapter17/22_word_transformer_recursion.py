def f(src, dst, words):
  if not words: return ()
  is_valid, nbor1chr = get_nbor1chr(
            words, src, dst)
  if not is_valid: return ()
  from collections import deque
  path, visited = deque(), set()
  g(dst, nbor1chr, path, visited, src)
  return (*path,)

def g(dst, nbor1chr, path, visited, src):
  visited.add(src)
  if src == dst:
    path.appendleft(src)
    return True

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
      if nbor not in visited:
        yield nbor


def get_nbor1chr(words, src, dst):
  seen_src = False; seen_dst = False
  from collections import defaultdict
  nbor1chr = defaultdict(set)
  n = len(words[0])
  for word in words:
    seen_src |= word == src
    seen_dst |= word == dst
    for i in range(n):
      key = f'{word[:i]}*{word[i + 1:]}'
      nbor1chr[key].add(word)

  return (seen_src and seen_dst, nbor1chr)

assert f('DAMP', 'DAMP', ()) == ()
assert f('DAMP', 'DAMP', ('DAMP',)) == ('DAMP',)
assert f('DAMP', 'LIKE', (
  'LIMP', 'LAMP', 'DAMP', 'LIKE', 'LIME')) == (
    'DAMP', 'LAMP', 'LIMP', 'LIME', 'LIKE')
assert f('DAMP', 'LIKE', (
  'DMMP', 'LAMP', 'LIMP', 'LIME', 'LIKE')) == ()

# time O(NLM)
# space O(NL)
# where N is number of words, L is length of words, and M is the cardinality of the character set
