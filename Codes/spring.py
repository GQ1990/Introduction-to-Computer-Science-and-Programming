import matplotlib.pylab as plt
import math


def rSquare(measured, estimated):
    diffs = (estimated - measured) ** 2
    mMean = measured.sum() / len(measured)
    var = (mMean - measured) ** 2
    return 1 - diffs.sum() / var.sum()


# Get data from file
def getData(fname):
    f = open(fname, 'r')
    X = []
    Y = []
    f.readline()  # ignore header
    for line in f:
        # if line[0] == '#':
        #     continue
        line = line[:-1]
        elems = line.rsplit(' ')
        X.append(float(elems[0]))
        Y.append(float(elems[1]))
    return plt.array(X), plt.array(Y)


if __name__ == '__main__':
    times, speeds = getData('springData.txt')

    # Analyze data
    plt.scatter(times, speeds)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Speed')

    a, b = plt.polyfit(times, speeds, 1)
    yVals = a * times + b
    plt.plot(times, yVals, color='g', linewidth=2, label='Linear')
    plt.title('Speed Versus Time')
    plt.legend()

    a, b, c = plt.polyfit(times, speeds, 2)
    yVals = a * (times ** 2) + b * times + c
    plt.plot(times, yVals, c='r', linewidth=4, label='Quadratic')
    plt.legend()

    plt.show()

    print(input('Enter anything to finish the program'))
