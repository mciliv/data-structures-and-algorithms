# Time: O(2 ^ n)
# Space: O(2 ^ n)
def fibonacci_recursive(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)

# Time: O(n)
# Space: O(n)
def fibonacci_memoized(num):
    fibonaccis = [0, 1]
    i = 2
    while i <= num:
        fibonaccis.append(fibonaccis[i-1] + fibonaccis[i-2])
        i += 1
    return fibonaccis[num]

# Time: O(n)
# Time: O(1)
def fibonacci(num):
    first = 0
    second = 1

    if num == 0:
        return first
    elif num == 1:
        return second
    else:
        i = 2
        while i <= num:
            new = first + second
            first = second
            second = new
            i += 1

    return new





assert(fibonacci_recursive(0) == 0)
assert(fibonacci_recursive(1) == 1)
assert(fibonacci_recursive(2) == 1)
assert(fibonacci_recursive(3) == 2)
assert(fibonacci_recursive(4) == 3)
assert(fibonacci_recursive(5) == 5)
assert(fibonacci_memoized(0) == 0)
assert(fibonacci_memoized(1) == 1)
assert(fibonacci_memoized(2) == 1)
assert(fibonacci_memoized(3) == 2)
assert(fibonacci_memoized(4) == 3)
assert(fibonacci_memoized(5) == 5)
assert(fibonacci(0) == 0)
assert(fibonacci(1) == 1)
assert(fibonacci(2) == 1)
assert(fibonacci(3) == 2)
assert(fibonacci(4) == 3)
assert(fibonacci(5) == 5)

        #
        #         5
        #     /     \
        #    4       3
        #   / \    /  \
        #  3   2    2  1
        #  /\ /\    /\  /\
        # 2 1 1 0  1 0 1 0
