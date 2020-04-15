import matplotlib.pylab as plt
import numpy as np
import random

# 曲线图
plt.plot([1, 2, 3, 4])
plt.plot([5, 6, 7, 8])
plt.figure()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# 点图
plt.figure()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.title('Earnings')
plt.xlabel('Days')
plt.ylabel('Dollars')
plt.figure()
xAxis = np.array([1, 2, 3, 4])
print(xAxis)
test = np.arange(1, 5)
print(test)
print(test == xAxis)
yAxis = xAxis ** 3
plt.plot(xAxis, yAxis, 'ro')

# 直方图
plt.figure()
vals = []
dieVals = [1, 2, 3, 4, 5, 6]
for i in range(10000):
    vals.append(random.choice(dieVals) + random.choice(dieVals))
plt.hist(vals, bins=11)

plt.show()
