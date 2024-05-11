# f :: String -> [String]

# Write a method to compute all permutations of
# a string of unique characters

def g(C):
    if not C:
        yield ''
        return
    for subperm in g(C[1:]):
        for i in range(len(C)):
            yield subperm[:i] + C[0] + subperm[i:]

f = lambda s: (*g(s),)

assert f('') == ('',)
assert f('a') == ('a',)
assert f('ab') == ('ab', 'ba')
assert f('abc') == ('abc', 'bac', 'bca',
                    'acb', 'cab', 'cba')

# Time: O(n!)
# Space: O(n)
# where n == len(C)
