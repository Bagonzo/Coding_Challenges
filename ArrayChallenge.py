# Array Challenge
# Have the function
# ArrayChallenge (arr) take the
# array of numbers stored in arr and
# return the string true if any
# combination of numbers in the array
# (excluding the largest number) can be
# added up to equal the largest number
# in the array, otherwise return the
# string false. For example: if arr
# contains [4, 6, 23, 10, 1, 3] the output
# should return true because 4 + 6 + 10
# +3 = 23. The array will not be empty,
# will not contain all the same
# elements, and may contain negative
# numbers.
# Examples
# Input: [5,7,16,1,2]
# Output: false

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