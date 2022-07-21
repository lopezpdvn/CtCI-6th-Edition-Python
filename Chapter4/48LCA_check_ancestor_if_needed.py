def f(bt, p, q):

    seen = {}

    lca = get_lca(p, q, seen, bt)
    if seen.get('p') and seen.get('q'):
        return lca

    if not seen.get('p') and not seen.get('q'):
        return None

    if not lca:
        return lca

    if not seen.get('q'):
        seen['q'] = is_ancestor(bt, q)

    if not seen.get('p'):
        seen['p'] = is_ancestor(bt, p)

    if seen.get('p') and seen.get('q'):
        return lca

    return None

def get_lca(p, q, seen, bt):
    if not bt:
        return bt

    if bt == p:
        seen['p'] = True
        return bt

    if bt == q:
        seen['q'] = True
        return bt

    llca = get_lca(p, q, seen, bt.left)
    rlca = get_lca(p, q, seen, bt.right)

    if llca and rlca:
        return bt

    return llca if llca else rlca


def is_ancestor(bt, x):
    if not bt or not x:
        return True

    if bt == x:
        return True

    return is_ancestor(bt.left, x) or is_ancestor(bt.right, x)
