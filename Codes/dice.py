import random
import matplotlib.pylab as plt

fair = [1, 2, 3, 4, 5, 6]


def throwPair(vals1, vals2):
    d1 = random.choice(vals1)
    d2 = random.choice(vals2)
    return d1, d2


def conductTrials(numThrows, die1, die2):
    throws = []
    for i in range(numThrows):
        d1, d2 = throwPair(die1, die2)
        throws.append(d1 + d2)
    return throws


def craps(die1, die2):
    d1, d2 = throwPair(die1, die2)
    tot = d1 + d2
    if tot in [7, 11]:
        return True
    if tot in [2, 3, 12]:
        return False
    point = tot
    while True:
        d1, d2 = throwPair(die1, die2)
        tot = d1 + d2
        if tot == point:
            return True
        if tot == 7:
            return False


def winCraps(numSets, die1, die2):
    wins, loses = [0, 0]
    for i in range(numSets):
        if craps(die1, die2):
            wins += 1
        else:
            loses += 1
    print(wins, loses)
    houseWin = loses / numSets
    print(houseWin)


if __name__ == '__main__':

    numThrows = 100000

    throws = conductTrials(numThrows, fair, fair)
    plt.hist(throws, 11)
    plt.xticks(range(2, 13), ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    plt.title('Distribution of Values')
    plt.xlabel('Sum of two die')
    plt.ylabel('Number of Throws')

    # Get probabilities for fair dice
    plt.figure()
    sums = plt.array([0] * 14)
    for val in range(2, 13):
        sums[val] = throws.count(val)
    probs = sums[2:13] / numThrows
    xVals = plt.arange(2, 13)
    plt.plot(xVals, probs, label='Fair Dice')
    plt.xticks(range(2, 13), ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    plt.title('Probability of a Value')
    plt.xlabel('Sum of Two Die')
    plt.ylabel('Probability')
    plt.show()

    # pair = [1, 2, 3, 4, 5, 6]
    # winCraps(100000, pair, pair)
