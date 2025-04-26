# Arrays (Zero Sum Subarray)
# Given an array of integers, find a subarray that sums to zero.
# Example:
# Input: [1, 2, -3, 4, -1]
# Output: [2, -3, 4, -1]
# Explanation: The subarray [2, -3, 4, -1] sums to zero.
# Approach:
# 1. Initialize an empty set to store the prefix sums.
# 2. Initialize a variable to store the current sum.
# 3. Iterate through the array and update the current sum.
# 4. If the current sum is zero, return the subarray from the start to the current index.
# 5. If the current sum is already in the set, return the subarray from the index of the first occurrence of the current sum to the current index.
# 6. Otherwise, add the current sum to the set.
# 7 . If no subarray is found, return False.
# Time Complexity: O(n)
# Space Complexity: O(n)


def zero_sum_subarray(nums):
   sums =set([0])
   current_sum = 0

   for num in nums:
     current_sum += num
     if current_sum in sums:
        return True
     sums.add(current_sum)
   return False

example_array = [1, 2, -3, 4, -1]
result = zero_sum_subarray(example_array)
if result:
    print("Subarray with zero sum found.")
else:
    print("No subarray with zero sum found.")