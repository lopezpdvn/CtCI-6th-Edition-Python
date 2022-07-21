def f(x, p, q):
  if (   not is_ancestor(x, p)
    or not is_ancestor(x, q):
    return None

  return g(x, p, q)

def g(x, p, q):
  if x is None or x.val == p.val or x.val == q.val:
    return x
  is_left_p_anc = is_ancestor(x.left, p)
  is_left_q_anc = is_ancestor(x.left, q)

  if is_left_p_anc and is_left_q_anc:
    return g(x.left, p, q)
  elif is_left_p_anc or is_left_q_anc:
    return x
  return g(x.right, p, q)

def is_ancestor(p, q):
  if p is None: return False
  if q is None: return True
  return (   p.value == q.value
      or is_ancestor(p.left, q)
      or is_ancestor(p.right, q))
