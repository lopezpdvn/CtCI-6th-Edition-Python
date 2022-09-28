def f(p, q):
    if not (p and q): return None
    if p == q: return p
    p_last = p
    p_size = 1
    while p_last.next:
        p_last = p_last.next
        p_size += 1
    q_last = q
    q_size = 1
    while q_last.next:
        q_last = q_last.next
        q_size += 1
    if p_last != q_last: return None
    sizes_diff = abs(p_size - q_size)
    if p_size > q_last:
        longest_x = p
        shortest_x = q
    else:
        longest_x = q
        shortest_x = p
    for _ in range(sizes_diff):
        longest_x = longest_x.next
    while longest_x != shortest_x:
        longest_x = longest_x.next
        shortest_x = shortest_x.next
    return longest_x
