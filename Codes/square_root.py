def square_root_bi(x, epsilon):
    """Bi-section solution"""
    assert x >= 0, 'x must be non-negative, not' + str(x)
    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
    low = 0
    high = max(x, 1.0)
    guess = (low + high) / 2.0
    ctr = 1
    while abs(guess ** 2 - x) > epsilon and ctr <= 100:
        if guess ** 2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print('Bi method. Num iterations:', ctr, 'Estimate:', guess)
    return guess


def square_root_nr(x, epsilon):
    """
    Newton-Raphson solution
    """
    assert x >= 0, 'x must be non-negative, not' + str(x)
    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
    x = float(x)
    guess = x / 2.0
    # guess = 0.001
    diff = guess ** 2 - x
    ctr = 1
    while abs(diff) > epsilon and ctr <= 100:
        guess = guess - diff / (2.0 * guess)
        diff = guess ** 2 - x
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print('NR method. Num iterations:', ctr, 'Estimate:', guess)
    return guess


if __name__ == '__main__':
    square_root_bi(6, 0.000001)
    square_root_nr(6, 0.000001)



