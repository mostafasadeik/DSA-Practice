# Recursion (Product Sum)
# Write a function that takes in a "special" array and returns its product sum.
# A "special" array is a non-empty array that contains either integers or other "special" arrays.
# The product sum of a "special" array is the sum of its elements, where each integer is multiplied by its depth in the array.

# Approach:

def productSum(array, depth=1):
    total = 0
    for element in array:
        if type(element) is list: 
            total += productSum(element, depth + 1)
        else: 
            total += element
    return total * depth 


# Test cases
print(productSum([1, 2, [3, 4]]))  # Output: 17
print(productSum([1, [2, [3, 4]]]))  # Output: 21