# Arrays (Smallest Difference)
# Given two arrays of integers, find the pair of numbers (one from each array) such that the absolute difference between them is closest to zero.
# Return the difference.
# The result return array with number from the first array in the first podition and the number from the second array in the second position.
# Example:
# Input: [1, 2, 3, 4, 5], [10, 20, 30, 40, 50]
# Output: [5, 10]

def smallest_difference(arr1, arr2):
    if not arr1 or not arr2:
        return []

    arr1.sort()
    arr2.sort()
    i, j = 0, 0
    min_diff = float('inf')
    result = []
    
    while i < len(arr1) and j < len(arr2):
        a, b = arr1[i], arr2[j]
        diff = abs(a - b)
        
        if diff < min_diff:
            min_diff = diff
            result = [a, b]
        
        if a < b:
            i += 1
        else:
            j += 1
    
    return result 

# Example usage
arr1 = [-1,5,10,20,28,3]      
arr2 = [26,134,135,15,17]
result = smallest_difference(arr1, arr2)
print(result)  # Output: [5, 10]