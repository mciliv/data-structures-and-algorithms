
def first_and_last(list):
    if len(list) <= 0:
        return []
    elif len(list) <= 2:
        return list
    else:
        return [list[0], list[-1]]

assert(first_and_last([]) == [])
assert(first_and_last([3]) == [3])
assert(first_and_last([8, 3]) == [8, 3])
assert(first_and_last([8, 9, 5, 2, 3, 6]) == [8, 6])
