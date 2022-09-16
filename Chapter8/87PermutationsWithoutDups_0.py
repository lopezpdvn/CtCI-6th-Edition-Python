# f :: String -> [String]

# Write a method to compute all permutations of
# a string of unique characters

def f(s):
    if not s:
        yield ''
        return
    c = s[0]
    for suffix in f(s[1:]):
        for i in range(len(suffix) + 1):
            yield ''.join(
                      (suffix[:i], c, suffix[i:]))

g = lambda s: (*f(s),)

assert g('') == ('',)
assert g('a') == ('a',)
assert g('ab') == ('ab', 'ba')
assert g('abc') == ('abc', 'bac', 'bca',
                    'acb', 'cab', 'cba')
