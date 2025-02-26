def g(s):
    from collections import Counter
    yield from h(len(s), Counter(s), '')

def h(slen, mset, perm):
    if len(perm) == slen:
        yield perm
        return
    for char, count in mset.items():
        if not count: continue
        mset[char] = count - 1
        yield from h(slen, mset, perm + char)
        mset[char] = count

f = lambda s: (*g(s),)

assert f('') == ('',)
assert f('aaa') == ('aaa',)
assert f('aaab') == ('aaab', 'aaba', 'abaa', 'baaa')
