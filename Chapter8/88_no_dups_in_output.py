from collections import Counter

def f(s):
    mset = Counter(s)
    ans = []
    g('', mset, len(s), ans)
    return ans

def g(prefix, mset, remaining, ans):
    if not remaining:
        ans.append(prefix)
        return

    for c, count in mset.items():
        if not count:
            continue

        mset[c] = count - 1
        g(prefix + c, mset, remaining - 1, ans)
        mset[c] = count

y = f('aaabb')
print('Count: {0}'.format(len(y)))
for x in y:
    print(x)

# Count: 10
# aaabb
# aabab
# aabba
# abaab
# ababa
# abbaa
# baaab
# baaba
# babaa
# bbaaa
