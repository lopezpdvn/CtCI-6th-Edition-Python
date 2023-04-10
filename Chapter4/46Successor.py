# Time O(height)
# Space O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.value)

def f(node):
    if not node: return node

    if node.right:
        return get_left_most(node.right)

    while node and node.parent and node == node.parent.right:
        node = node.parent

    print(node.parent)
    return node.parent if node else None

def get_left_most(node):
    if not node:
        return None

    while node.left:
        node = node.left

    return node
