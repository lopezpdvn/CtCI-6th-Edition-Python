def f(a, b):
    if not a or not b: return None
    ah, alen, bh ,blen = a, 1, b, 1

    while a.next:
        alen += 1
        a = a.next

    while b.next:
        blen += 1
        b = b.next

    if a != b: return None
    a, b = ah, bh

    for i in range(abs(alen - blen)):
        if alen >= blen:
            a = a.next
        else:
            b = b.next

    for i in range(min(alen, blen)):
        if a == b:
            return a
        else:
            a, b = a.next, b.next

import unittest

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class TestIntersection(unittest.TestCase):
    def test_no_intersection(self):
        a1, a2, a3 = Node(1), Node(2), Node(3)
        b1, b2, b3 = Node(4), Node(5), Node(6)
        a1.next, a2.next = a2, a3
        b1.next, b2.next = b2, b3
        self.assertIsNone(f(a1, b1))

    def test_intersection_same_tail(self):
        c1, c2, c3, c4 = Node(1), Node(2), Node(3), Node(4)
        d1, d2 = Node(5), Node(6)
        c1.next, c2.next, c3.next = c2, c3, c4
        d1.next = d2
        d2.next = c3
        self.assertEqual(f(c1, d1), c3)

    def test_intersection_equal_length(self):
        e1, e2, e3 = Node(7), Node(8), Node(9)
        f1, f2, f3 = Node(10), Node(11), Node(12)
        e1.next, e2.next = e2, e3
        f1.next, f2.next = f2, f3
        f3.next = e3
        self.assertEqual(f(e1, f1), e3)

if __name__ == "__main__":
    unittest.main()
