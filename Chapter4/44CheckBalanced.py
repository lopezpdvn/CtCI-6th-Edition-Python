from math import inf

def f(p):
    return get_height(p) != -inf

def get_height(p):
    if p is None: return -1
    left_branch_h = get_height(p.left)
    if left_branch_h == -inf: return -inf
    right_branch_h = get_height(p.right)
    if right_branch_h == -inf: return -inf

    if abs(left_branch_h - right_branch_h) > 1:
        return -inf

    return max(left_branch_h, right_branch_h) + 1
