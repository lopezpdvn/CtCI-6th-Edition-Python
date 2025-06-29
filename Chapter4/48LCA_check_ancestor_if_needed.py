def f(x, a, b):
    if not x:
        if not a and not b: return x
        else: raise Exception()
    if a and not b:
        lca = get_node(x, a)
        if lca: return lca
        else: raise Exception()
    if b and not a:
        lca = get_node(x, b)
        if lca: return lca
        else: raise Exception()
    if not a and not b: return deepest_leaf(x)

    seen = {'a': None, 'b': None}
    lca = get_lca(seen, a, b, x)
    if not lca: raise Exception()
    seen['a'] = seen.get('a', get_node(x, a))
    seen['b'] = seen.get('b', get_node(x, b))
    if seen['a'] and seen['b']: return lca
    raise Exception()

def get_lca(seen, a, b, x):
    if not x: return x
    if x == a:
        seen['a'] = a
        return x
    if x == b:
        seen['b'] = b
        return x
    llca = get_lca(seen, a, b, x.left)
    rlca = get_lca(seen, a, b, x.right)
    if llca and rlca: return x
    return llca or rlca
