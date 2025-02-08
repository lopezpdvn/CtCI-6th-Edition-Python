def g(x):
    if not x: return (None, True)
    lh, lisb = g(x.left)
    if not lisb: return (None, False)
    rh, risb = g(x.right)
    if not risb: return (None, False)
    return (1 + max(lh, rh), abs(lh - rh) <= 1)

def f(x):
    _, isb = g(x)
    return isb
