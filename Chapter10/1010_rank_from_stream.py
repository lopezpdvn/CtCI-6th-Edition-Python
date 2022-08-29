class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.lsize = 0
        self.rsize = 0

    def get_rank(self, value):
        if self.value == value: return self.lsize
        if value < self.value:
            return (self.left.get_rank(value)
                if self.left else -1)
        rrank = (self.right.get_rank(value)
            if self.right else -1)
        lrank = self.lsize or 0
        return rrank if rrank < 0 else 1 + lrank + rrank

    def track(self, value):
        if value <= self.value:
            self.lsize += 1
            if self.left:
                self.left.track(value)
            else:
                self.left = BSTNode(value)
        else:
            self.rsize += 1
            if self.right:
                self.right.track(value)
            else:
                self.right = BSTNode(value)

class DS:
    def __init__(self, *es):
        self.root = None
        for e in es:
            self.track(e)

    def track(self, e):
        if not self.root:
            self.root = BSTNode(e)
        else:
            self.root.track(e)

    def get_rank(self, value):
        if not self.root: return -1
        return self.root.get_rank(value)

x = DS(5,1,4,4,5,9,7,13,3)
assert x.get_rank(1) == 0
assert x.get_rank(3) == 1
assert x.get_rank(4) == 3
