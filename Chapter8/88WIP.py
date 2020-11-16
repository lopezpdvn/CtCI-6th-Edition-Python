from collections import Counter

def f(s):
    mset = Counter(s)
    ans = []
    g(s, '', mset, len(s), ans)
    return ans

def g(s, prefix, mset, remaining, ans):
    if not remaining:
        ans.append(prefix)

    for c, count in mset.items():
        if not count:
            continue

        mset[c] = count - 1
        g(s, prefix + c, mset, remaining - 1, ans)
        mset[c] = count
