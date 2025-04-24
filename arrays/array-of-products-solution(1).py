# Arrays (Array of Products)
# Given an array of integers, write a function that returns an array of the same length where each element at index i is the product of all the numbers in the original array except the one at i.
# The problem is to find the product of all elements in an array except the one at the current index.
# The function should return an array of the same length where each element at index i is the product of all the numbers in the original array except the one at i.
# Sample Input
# array = [1, 2, 3, 4]
# Sample Output
# [24, 12, 8, 6]
# Approach
# 1. Initialize an empty result array of the same length as the input array.        
# 2. Iterate through the input array and calculate the product of all elements to the left of the current index.
# 3. Store the product in the result array at the current index.
# 4. Iterate through the input array in reverse order and calculate the product of all elements to the right of the current index.
# 5. Multiply the product of the right elements with the corresponding element in the result array.
# 6. Return the result array.

def array_of_products(array):
    products = [1] * len(array)

    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j:
                runningProduct *= array[j]
        products[i] = runningProduct
        
    return products


# Test the function with different inputs
array = [1, 2, 3, 4]
print(array_of_products(array))  # Output: [24, 12, 8, 6]