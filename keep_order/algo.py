def keep_order(ary, val):
    if ary == []:
        return 0
    return min([i if x >= val else len(ary) for i, x in enumerate(ary)])
