def fib(n):
    """Fibonacci"""
    global numCalls
    numCalls += 1
    # print('fib called with', n)
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fast_fib(n, memo):
    """fast edition of Fibonacci"""
    global numCalls
    numCalls += 1
    if n not in memo:
        memo[n] = fast_fib(n - 1, memo) + fast_fib(n - 2, memo)
    return memo[n]


def fib1(n):
    """Fibonacci"""
    memo = {0: 1, 1: 1}
    return fast_fib(n, memo)


if __name__ == '__main__':
    number = 0
    numCalls = 0
    result = fib(number)
    print('numCalls:', numCalls)
    print('fib(%d):%f' % (number, result))

    numCalls = 0
    result1 = fib1(number)
    print('numCalls:', numCalls)
    print('fib(%d):%f' % (number, result1))