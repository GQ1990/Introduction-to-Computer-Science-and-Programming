import matplotlib.pylab as plt
import random
import math
import numpy as np


def flipTrial(numFlips):
    heads, tails = 0, 0
    for i in range(0, numFlips):
        coin = random.randint(0, 1)
        if coin == 0:
            heads += 1
        else:
            tails += 1
    return heads, tails


def simFlips(numFlips, numTrials):
    diffs = []
    for i in range(0, numTrials):
        heads, tails = flipTrial(numFlips)
        diffs.append(abs(heads - tails))
    diffs = np.array(diffs)
    diffMean = sum(diffs) / len(diffs)
    diffPercent = (diffs / float(numFlips)) * 100
    percentMean = sum(diffPercent / len(diffPercent))
    plt.hist(diffs)
    plt.axvline(diffMean, label='Mean')
    plt.legend()
    titleString = str(numFlips) + ' Flips,' + str(numTrials) + ' Trials'
    plt.title(titleString)
    plt.xlabel("Difference between heads and tails")
    plt.ylabel("Number of Trials")

    plt.figure()
    plt.plot(diffPercent)
    plt.axhline(percentMean, label='Mean')
    plt.legend()
    plt.title(titleString)
    plt.xlabel("Trial Numbers")
    plt.ylabel("Difference between heads and tails")


if __name__ == '__main__':
    simFlips(3, 10)
    plt.show()
