# Arrays (Three Number Sum)
# Given an array of integers, the task is to find all unique triplets in the array that sum up to zero.
# The function threeNumberSum takes an array of integers as input and returns a list of lists, where each inner list contains three integers that sum up to zero.
# The function uses a two-pointer approach to find the triplets efficiently.
# The time complexity of this solution is O(n^2), where n is the length of the input array.
# The space complexity is O(k), where k is the number of unique triplets found.
# Approach:
# 1. Sort the input array to make it easier to find triplets.
# 2. Initialize an empty list to store the triplets.
# 3. Iterate through the array using a for loop.
# 4. For each element, use two pointers to find the other two elements that sum up to zero.
# 5. If the sum of the three elements is zero, add the triplet to the result list.
# 6. Move the left and right pointers to find other potential triplets.
# 7. Skip duplicate elements to avoid duplicate triplets.
# 8. Return the list of unique triplets.

def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets
# Example usage
array = [12,3,1,2,-6,5,-8,6]
targetSum = 0
result = threeNumberSum(array, targetSum)   
print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]