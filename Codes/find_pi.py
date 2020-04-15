import matplotlib.pylab as plt
import random
import math
import numpy as np


def throwDarts(numDarts):
    inCircle = 0
    for darts in range(1, numDarts + 1):
        x = random.random()
        y = random.random()
        if (x * x + y * y) ** 0.5 <= 1:
            inCircle += 1
    return 4 * (inCircle / numDarts)


def get_est(numDarts, numTrials):
    estimates = []
    for t in range(numTrials):
        pi_guess = throwDarts(numDarts)
        estimates.append(pi_guess)
    sdev = np.std(estimates)
    pi_est = sum(estimates) / len(estimates)
    print('Est. = ', str(round(pi_est, 5)) + ',',
          'Std. Dev. = ', str(round(sdev, 5)) + ',',
          'Darts = ', numDarts)
    return pi_est, sdev


def est_pi(precision, numDarts, numTrials):
    sdev = precision
    while sdev > precision / 1.96:
        pi_est, sdev = get_est(numDarts, numTrials)
        numDarts *= 2
    return pi_est


if __name__ == '__main__':
    est_pi(0.01, 1000, 100)
