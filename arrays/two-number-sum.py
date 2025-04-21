# Arrays - problem (Two Number Sum)

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example:
# Input: nums = [2,7,11,15], target = 9

def two_sum_brute_force(array, targetSum):
    n = len(array)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []

# Time complexity: O(n^2) — nested loops check every possible pair
# Space complexity: O(1) — no extra space used
# Brute-force approach: simple, but inefficient for large inputs


def two_sum_hash_map(array, targetSum):
    hashNums = {}
    for curr in array:
        complement = targetSum - curr
        if complement in hashNums:
            return [complement, curr]
        hashNums[curr] = True
    return []

# Time complexity: O(n) — single pass through the array
# Space complexity: O(n) — extra space for the hash table
# Hash map approach: fast and efficient, uses hashing to store complements



def two_sum_two_pointers(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        arraySum = array[left] + array[right]
        if arraySum == targetSum:
            return [array[left], array[right]]
        elif arraySum < targetSum:
            left += 1
        else:
            right -= 1
    return []


# Time complexity: O(n log n) — due to sorting the array
# Space complexity: O(1) — uses only two pointers
# Two pointers approach: efficient for sorted arrays, avoids extra space

result1 = two_sum_brute_force([4, 6, 1, 2], 5)
result2 = two_sum_hash_map([3,9,2,7,7,6], 11)
result3 = two_sum_two_pointers([1,9,2,7,6,4,8,9,-1], 5)

print(result1) 
print(result2) 
print(result3) 





