# f :: String -> [String]

# Write a method to compute all permutations of
# a string of unique characters

def g(s):
    if not s:
        yield ''
        return
    c = s[0]
    for subperm in g(s[1:]):
        for i in range(len(subperm) + 1):
            yield subperm[:i] + c + subperm[i:]

f = lambda s: (*g(s),)

assert f('') == ('',)
assert f('a') == ('a',)
assert f('ab') == ('ab', 'ba')
assert f('abc') == ('abc', 'bac', 'bca',
                    'acb', 'cab', 'cba')
