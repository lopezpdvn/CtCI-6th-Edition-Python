class BSTNode:
  def __init__(self, value, L=None,R=None):
    self.value = value
    self.L = L
    self.R = R
    self.lsize = 0
    self.rsize = 0

  def get_rank(self, value):
    if self.value == value: return self.lsize
    if value < self.value:
      return (self.L.get_rank(value)
              if self.L else 0)

    rrank = (self.R.get_rank(value)
             if self.R else 0)
    return self.lsize + 1 + rrank

  def track(self, value):
    if value <= self.value:
      self.lsize += 1
      if self.L:
        return self.L.track(value)
      else:
        self.L = BSTNode(value)
        return self.L
    else:
      self.rsize += 1
      if self.R:
        return self.R.track(value)
      else:
        self.R = BSTNode(value)
        return self.R

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
    return (self.root.get_rank(value)
            if self.root else 0)


x = DS(5,1,4,4,5,9,7,13,3)
assert x.get_rank(1) == 0
assert x.get_rank(3) == 1
assert x.get_rank(4) == 3

x = DS(5,1,4,4,5,9,7)
assert x.get_rank(-1) == 0
assert x.get_rank(5) == 4
assert x.get_rank(7) == 5
assert x.get_rank(8) == 6
assert x.get_rank(10) == 7
assert x.get_rank(9999) == 7
