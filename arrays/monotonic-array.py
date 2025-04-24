# Arrays (Monotonic Array)
# Given an array of integers, write a function that returns true if the array is monotonic (i.e., it is either entirely non-increasing or non-decreasing).
# A monotonic array is an array that is either entirely non-increasing or non-decreasing.
# An array is non-increasing if its elements are in decreasing order or equal to each other.
# An array is non-decreasing if its elements are in increasing order or equal to each other.
# The function should return true if the array is monotonic and false otherwise.
# Sample Input
# array = [1, 2, 2, 3, 4]
# Sample Output
# True

#Approach

def isMonotonic(array):
    if len(array) < 2:
        return True

    increasing = decreasing = True

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            decreasing = False
        elif array[i] < array[i - 1]:
            increasing = False
    return increasing or decreasing


# Test the function with different inputs
array = [1, 2, 2, 3, 4]
print(isMonotonic(array))  # Output: True