def f(s):
    if not s:
        yield ''
        return
    from collections import Counter
    yield from g(len(s), Counter(s), '')

def g(perm_len, mset, prefix):
    if len(prefix) == perm_len:
        yield prefix
        return

    for char, count in mset.items():
        if not count:
            continue
        mset[char] = count - 1
        yield from g(perm_len, mset, prefix + char)
        mset[char] = count

assert (*f(''),) == ('',)
assert (*f('aaa'),) == ('aaa',)
assert (*f('aaab'),) == ('aaab', 'aaba', 'abaa', 'baaa')
