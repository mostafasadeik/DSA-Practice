# Arrays (Sorted Squared Array)
# Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.
#
# Sample Input: 
# array = [1, 2, 3, 5, 6, 8,9]
# Sample Output:
# squared_array = [1, 4, 9, 25, 36, 64, 81]
#
# Approach:
# 1. Initialize an empty array to store the squared values.
# 2. Iterate through the input array and square each element.
# 3. Append the squared values to the new array.
# 4. Sort the new array in ascending order.
# 5. Return the new sorted array.
# 6. Time complexity: O(n log n) where n is the length of the input array.
# 7. Space complexity: O(n) since we are creating a new array to store the squared values.

def sorted_squared_array(array):
    squared_array = [0 for _ in array]
    for num in range(len(array)):
        value = array[num]
        squared_array[num] = value * value
    # Sort the squared array
    squared_array.sort()
    return squared_array

def sorted_squared_array_direct(array):
    squared_array = [x * x for x in array]
    squared_array.sort()
    return squared_array



# Example usage
result1 = sorted_squared_array([1, 2, 3, 5, 6, 8, 9])
result2 = sorted_squared_array_direct([1, 2, 3,])
print(result1)  # Output: [1, 4, 9, 25, 36, 64, 81]
print(result2)  # Output: [1, 4, 9, 25, 36, 64, 81]



# Difference between for i in range(len(array)) and for i in array
# 1. for i in range(len(array)):
#    - This iterates over the indices of the array.
#    - The variable i takes on the values 0, 1, 2, ..., len(array)-1.
#    - You can use i to access the elements of the array using array[i].
# 2. for i in array:
#    - This iterates directly over the elements of the array.
#    - The variable i takes on the values of the elements in the array.
#    - You can use i directly without needing to access it through an index.

