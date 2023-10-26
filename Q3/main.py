import random
import time
import matplotlib.pyplot as plt
from sortedcontainers import SortedDict

def generateRandomList(n):
    random_list = [random.randint(0, n) for _ in range(n)]
    return random_list

def measureBinaryTreeInsertionTime(n):
    keys = list(range(n))
    random.shuffle(keys)
    data = generateRandomList(n)
    bt = SortedDict()
    startTime = time.time()

    for i in range(n):
        bt[keys[i]] = data[i]

    endTime = time.time()
    return endTime - startTime

def measureHashTableInsertionTime(n):
    keys = list(range(n))
    random.shuffle(keys)
    data = generateRandomList(n)
    bt = dict()
    startTime = time.time()

    for i in range(n):
        bt[keys[i]] = data[i]

    endTime = time.time()
    return endTime - startTime

inputs = []
btInsertionTimes = []
hashInsertionTimes = []

for i in range(10000):
    print(i)
    INPUTSIZE = i

    inputs.append(INPUTSIZE)
    btInsertionTimes.append(measureBinaryTreeInsertionTime(INPUTSIZE))
    hashInsertionTimes.append(measureHashTableInsertionTime(INPUTSIZE))

plt.plot(inputs, btInsertionTimes, label="Binary Tree Insertion")
plt.plot(inputs, hashInsertionTimes, label="Hash Table Insertion")
plt.xlabel("Input Size")
plt.ylabel("Time (s)")
plt.title("Binary Tree vs Hash Table Insertion")

plt.legend()

plt.show()

INPUTSIZE = 1000000
print("Hash table insertion time for " + str(INPUTSIZE) + " inputs: " + str(measureHashTableInsertionTime(INPUTSIZE)))
print("Binary tree insertion time for " + str(INPUTSIZE) + " inputs: " + str(measureBinaryTreeInsertionTime(INPUTSIZE)))
# Hash table insertion time for 1000000 inputs: 0.2752652168273926
# Binary tree insertion time for 1000000 inputs: 3.47869610786438
