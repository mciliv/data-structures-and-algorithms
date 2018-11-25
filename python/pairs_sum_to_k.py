# Given an integer array and a number k, output all pairs that sum up to k.

 # [0, 11, 8, 5, 9, 4, 10, 12, 3, 6, 2, 1] k = 5

# (0, 5) (4, 1) (3, 2)

def get_pairs_sum_to_k(integers, k):
    integer_set = set(integers)
    pairs_sum_to_k = set()

    for integer in integer_set:
        if k - integer in integer_set and \
            (k - integer, integer) not in pairs_sum_to_k:
           pairs_sum_to_k.add((integer, k - integer))

    return pairs_sum_to_k


print(get_pairs_sum_to_k([0, 11, 8, 5, 9, 4, 10, 12, 3, 6, 2, 1], 5))
