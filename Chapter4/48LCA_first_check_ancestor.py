def f(x, p, q):
  if (   not is_ancestor(x, p)
    or not is_ancestor(x, q):
    return None

  return g(x, p, q)

def common_ancestor(root, p, q):
    if root is None or root == p or root == q:
        return root

    left = common_ancestor(root.left, p, q)
    right = common_ancestor(root.right, p, q)

    # if one node is found on left and one on right, then root is their common ancestor
    if left and right:
        return root
    # otherwise, whichever side is non-null is the side where both nodes are
    return left or right

def is_ancestor(p, q):
  if p is None: return False
  if q is None: return True
  return (   p.value == q.value
      or is_ancestor(p.left, q)
      or is_ancestor(p.right, q))
