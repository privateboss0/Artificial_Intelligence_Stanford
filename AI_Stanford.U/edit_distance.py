def compute_edit_distance(s, t):
    def recurse(m, n):
        """Return the minimum edit distance between:
        - first m letters of s
        - first n letters of t"""
        if m == 0:
            return n
        elif n == 0:
            return m
        elif s[m - 1] == t[n - 1]:
            return recurse(m - 1, n - 1)
        else:
            sub_cost = 1 + recurse(m - 1, n - 1)
            del_cost = 1 + recurse(m - 1, n)
            ins_cost = 1 + recurse(m, n - 1)
            return min(sub_cost, del_cost, ins_cost)
    return recurse(len(s), len(t))

print(compute_edit_distance('a cat!', 'the cats!'))