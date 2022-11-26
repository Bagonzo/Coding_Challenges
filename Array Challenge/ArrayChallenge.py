from math import factorial
import itertools

l = []
numCombinations = []
largest = 0
pos = 0
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    l.append(int(input("Enter number " + str(i+1) + ": ")))
    if l[i] > largest:
        largest = l[i]
        pos = i

def ArrayChallenge(arr):
    global numCombinations, largest, pos
    for r in range(len(arr)+1):
        for combination in itertools.combinations(arr, r):
            numCombinations.append(combination)
    for i in range(len(numCombinations)):
        total = 0
        for j in range(len(numCombinations[i])):
            total += int(numCombinations[i][j])
            if total == largest:
                return True
    return False

l.remove(largest)
print(ArrayChallenge(l))