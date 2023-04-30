class BSTNode:
  def __init__(self, value, left=None,right=None):
    self.value = value
    self.left = left
    self.right = right
    self.lsize = 0
    self.rsize = 0

  def get_rank(self, value):
    if self.value == value: return self.lsize
    if value < self.value:
      return (self.left.get_rank(value)
              if self.left else 0)

    lrank = self.lsize or 0
    rrank = (self.right.get_rank(value)
             if self.right else 0)
    return lrank + 1 + rrank

  def track(self, value):
    if value <= self.value:
      self.lsize += 1
      if self.left:
        return self.left.track(value)
      else:
        self.left = BSTNode(value)
        return self.left
    else:
      self.rsize += 1
      if self.right:
        return self.right.track(value)
      else:
        self.right = BSTNode(value)
        return self.right

class DS:
  def __init__(self, *es):
    self.root = None
    for e in es:
      self.track(e)

  def track(self, e):
    if not self.root:
      self.root = BSTNode(e)
      return self.root
    else:
      return self.root.track(e)

  def get_rank(self, value):
    if not self.root: return 0
    return self.root.get_rank(value)


x = DS(5,1,4,4,5,9,7,13,3)
assert x.get_rank(1) == 0
assert x.get_rank(3) == 1
assert x.get_rank(4) == 3

x = DS(5,1,4,4,5,9,7)
assert x.get_rank(-1) == 0
assert x.get_rank(5) == 4
assert x.get_rank(7) == 5
assert x.get_rank(8) == 6   # not in tree
assert x.get_rank(10) == 7  # not in tree
assert x.get_rank(9999) == 7  # not in tree
