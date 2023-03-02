def longest(a1, a2):
    longest = ""
    for i in sorted(list(set([*a2] + [*a1])), reverse=False):
        longest = longest + i
    return longest

def longest_simplify(a1, a2):
    return "".join(sorted(set(a1 + a2)))
