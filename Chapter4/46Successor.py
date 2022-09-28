def f(x):
    if not x:
        return None

    if x.right:
        x = x.right
        while x.left:
            x = x.left
        return x

    while x.parent and x.parent.left != x:
        x = x.parent

    return x.parent
