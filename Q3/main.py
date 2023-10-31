import random
import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.val:
            if not node.left:
                node.left = Node(val)
            else:
                self._insert(val, node.left)
        elif val == node.val:
            return
        else:
            if not node.right:
                node.right = Node(val)
            else:
                self._insert(val, node.right)

def generateRandomList(n):
    random_list = [random.randint(0, n) for _ in range(n)]
    return random_list

def measureBinaryTreeInsertionTime(n):
    keys = generateRandomList(n)
    random.shuffle(keys)
    data = generateRandomList(n)
    multimap = BST()
    startTime = time.perf_counter()

    for i in range(n):
        multimap.insert((keys[i], data[i]))

    endTime = time.perf_counter()
    return endTime - startTime

def measureHashTableInsertionTime(n):
    keys = list(range(n))
    random.shuffle(keys)
    data = generateRandomList(n)
    bt = dict()
    startTime = time.perf_counter()

    for i in range(n):
        bt[keys[i]] = data[i]

    endTime = time.perf_counter()
    return endTime - startTime

inputs = []
btInsertionTimes = []
hashInsertionTimes = []

for i in range(0, 50000, 500):
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
