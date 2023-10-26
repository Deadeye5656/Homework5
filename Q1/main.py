import time
import random
import matplotlib.pyplot as plt

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


def insertionSort(arr):
    n = len(arr)

    if n <= 1:
        return

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def generateRandomList(n):
    random_list = [random.randint(0, n) for _ in range(n)]
    return random_list

inputs = []
insertionTimes = []
mergeTimes = []

for i in range(1000):
    print(i)
    # INPUTSIZE = 100 + (i*100)
    INPUTSIZE = i
    randomList = generateRandomList(INPUTSIZE)
    randomListCopy = randomList.copy()

    startTime = time.time()
    insertionSort(randomList)
    endTime = time.time()
    insertionElapsedTime = endTime - startTime

    startTime = time.time()
    l = 0
    r = len(randomListCopy)-1
    mergeSort(randomListCopy, l, r)
    endTime = time.time()
    mergeElapsedTime = endTime - startTime

    if insertionElapsedTime > mergeElapsedTime:
        print(INPUTSIZE)

    inputs.append(INPUTSIZE)
    insertionTimes.append(insertionElapsedTime)
    mergeTimes.append(mergeElapsedTime)

plt.plot(inputs, insertionTimes, label="Insertion Sort")
plt.plot(inputs, mergeTimes, label="Merge Sort")
plt.xlabel("Input Size")
plt.ylabel("Time (s)")
plt.title("Insertion Sort vs Merge Sort")

plt.legend()

plt.show()

# Insertion sort starts being slower after 68 inputs