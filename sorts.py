"""
Various sort algorithms implemented in Python. All sorts can only take accept
an array of integers as parameters (for now...)
"""
import random

# Generates an unsorted array of random integers
# Params:   numElements - set number of elements in array
#           minVal - minimum element value (defaults to 0)
#           maxVal - maximum element value (defaults to 100)
def generateArray(numElements, minVal=0, maxVal=100):
    return [random.randrange(minVal,maxVal) for i in range(numElements)]

# O(n^2)
def insertionSort(array):
    for p in range(1,len(array)):
        temp = array[p]
        j = p
        while j > 0 and temp < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        array[j] = temp