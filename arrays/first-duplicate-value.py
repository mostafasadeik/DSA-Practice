# Arrays (First Duplicate Value)
# Given an array of integers, the task is to find the first duplicate value in the array.
# If there are no duplicates, return -1.
# The function first_duplicate_value takes an array of integers as input and returns the first duplicate value or -1 if there are no duplicates.
# The time complexity of this solution is O(n), where n is the length of the array.
# The space complexity is O(n) in the worst case, where all elements are unique.
# Approach:


def firstDuplicateValue(array):
    for value in array:
        absValue = abs(value)
        
        if absValue - 1 >= len(array):  
            continue  
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1

result = firstDuplicateValue([2, 9, 4,9, 2, 4, 4])
print(result)  # Output: 3