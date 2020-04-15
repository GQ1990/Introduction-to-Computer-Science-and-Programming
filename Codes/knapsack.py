def maxVal(w, v, i, aW):
    """
    Decision Tree for knapsack problem(0,1)
    w:  weights
    v:  value
    i:  number of items
    aW: maximum weight
    """
    # print('maxVal called with:', i, aW)
    global numCalls
    numCalls += 1
    if i == 0:
        if w[i] <= aW:
            return v[i]
        else:
            return 0
    without_i = maxVal(w, v, i - 1, aW)
    if w[i] > aW:
        return without_i
    else:
        with_i = v[i] + maxVal(w, v, i - 1, aW - w[i])
    return max(with_i, without_i)


def fast_maxVal(w, v, i, aW, m):
    """Decision Tree for knapsack problem(0,1), fast edition"""
    global numCalls
    numCalls += 1
    try:
        return m[(i, aW)]
    except KeyError:
        if i == 0:
            if w[i] <= aW:
                m[(i, aW)] = v[i]
                return v[i]
            else:
                m[(i, aW)] = 0
                return 0
        without_i = fast_maxVal(w, v, i - 1, aW, m)
        if w[i] > aW:
            m[(i, aW)] = without_i
            return without_i
        else:
            with_i = v[i] + fast_maxVal(w, v, i - 1, aW - w[i], m)
        res = max(with_i, without_i)
        m[(i, aW)] = res
        return res


def maxVal0(w, v, i, aW):
    m = {}
    return fast_maxVal(w, v, i, aW, m)


if __name__ == '__main__':
    weights = [1, 5, 3, 4]
    vals = [15, 10, 9, 5]
    numCalls = 0
    res = maxVal(weights, vals, len(vals) - 1, 8)
    print('max Val = ', res, 'Number of calls = ', numCalls)
    # weights = [1, 1, 5, 5, 3, 3, 4, 4]
    # vals = [15, 15, 10, 10, 9, 9, 5, 5]
    # numCalls = 0
    # res = maxVal(weights, vals, len(vals) - 1, 8)
    # print('max Val = ', res, 'number of calls = ', numCalls)
    # numCalls = 0
    # res = maxVal0(weights, vals, len(vals) - 1, 8)
    # print('max Val = ', res, 'number of calls = ', numCalls)
