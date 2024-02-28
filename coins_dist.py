import matplotlib.pyplot as plt
import numpy as np

np.random.seed(555)

tails_count = []

for distribution in range(10000) :
    tails = [0]
    for throws in range(10) :
        coin = np.random.randint(0, 2)
        tails.append(tails[throws] + coin)
    tails_count.append(tails[-1])

plt.hist(tails_count, bins=10)
plt.xlabel('Number of Tails')
plt.ylabel('Frequency')
plt.title('Histogram of Tails in 1000 Experiments with 10 Coin Tosses Each')
plt.show()
