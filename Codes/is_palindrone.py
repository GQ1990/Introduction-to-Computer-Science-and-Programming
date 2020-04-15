def silly():
    res = []
    done = False
    while not done:
        elem = input('Enter element. Return when done')
        if elem == ' ':
            done = True
        else:
            res.append(elem)
    tmp = res[:]
    tmp.reverse()
    print('tmp', tmp, 'res', res)
    isPal = (res == tmp)
    if isPal:
        print('is a palindrone')
    else:
        print('is NOT a palindrone')


if __name__ == '__main__':
    silly()
