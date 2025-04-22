# Arrays - Validate Subsequence

# Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
# A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative order of the remaining elements.
# (i.e., [1, 3, 4] is a subsequence of [1, 2, 3, 4] while [1, 4, 2] is not).
#
# Example:  
# Input: array = [5, 1, 22, 25, 6, -1, 8, 10], sequence = [1, 6, -1, 10]
# Output: True


# Approach:
# 1. Initialize two pointers, one for each array.
# 2. Iterate through the first array with the first pointer.
# 3. If the current element of the first array matches the current element of the second array, move the second pointer.
# 4. If the second pointer reaches the end of the second array, return True.
# 5. If the first pointer reaches the end of the first array and the second pointer has not reached the end of the second array, return False.
# 6. Time complexity: O(n) where n is the length of the first array.
# 7. Space complexity: O(1) since we are using only a constant amount of space.

def is_valid_subsequence_while(array, sequence):
    arrIndex = 0 
    seqIndex = 0
    while(arrIndex < len(array) and seqIndex < len(sequence)):
        if(array[arrIndex] == sequence[seqIndex]):
            seqIndex = seqIndex + 1
        arrIndex = arrIndex + 1
    return seqIndex == len(sequence)


def is_valid_subsequence_for(array,sequence):
    seqIndex=0
    for value in array:
       if (seqIndex < len(sequence) and value == sequence[seqIndex]):
            seqIndex += 1
    return seqIndex == len(sequence)

# Time complexity: O(n) where n is the length of the first array.
# Space complexity: O(1) since we are using only a constant amount of space.
# Example usage

result = is_valid_subsequence_while([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
print(result)  # Output: True
result = is_valid_subsequence_for([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 11])
print(result)  # Output: False