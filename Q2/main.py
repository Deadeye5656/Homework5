import time
import random
import matplotlib.pyplot as plt

def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


def timSort(arr):
    n = len(arr)
    minRun = 32

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)

    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size

def myMerge(arr, l, m, r):
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

def myMergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        myMergeSort(arr, l, m)
        myMergeSort(arr, m+1, r)
        myMerge(arr, l, m, r)


def myInsertionSort(arr):
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
timTimes = []

for i in range(1000):
    print(i)
    INPUTSIZE = i
    randomList = generateRandomList(INPUTSIZE)
    randomListCopy = randomList.copy()
    randomListCopyCopy = randomList.copy()

    startTime = time.time()
    myInsertionSort(randomList)
    endTime = time.time()
    insertionElapsedTime = endTime - startTime

    startTime = time.time()
    l = 0
    r = len(randomListCopy) - 1
    myMergeSort(randomListCopy, l, r)
    endTime = time.time()
    mergeElapsedTime = endTime - startTime

    startTime = time.time()
    timSort(randomListCopyCopy)
    endTime = time.time()
    timElapsedTime = endTime - startTime

    inputs.append(INPUTSIZE)
    insertionTimes.append(insertionElapsedTime)
    mergeTimes.append(mergeElapsedTime)
    timTimes.append(timElapsedTime)

plt.plot(inputs, insertionTimes, label="Insertion Sort")
plt.plot(inputs, mergeTimes, label="Merge Sort")
plt.plot(inputs, timTimes, label="Tim Sort")
plt.xlabel("Input Size")
plt.ylabel("Time (s)")
plt.title("Insertion Sort vs Merge Sort vs Tim Sort")

plt.legend()

plt.show()