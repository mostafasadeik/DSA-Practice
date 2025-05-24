# Searching (Find Three Largest Numbers)
# Find the three largest numbers in an array.

def findThreeLargestNumbers(array):
    threeLargest = [float('-inf')] * 3  # Initialize with negative infinity
    for num in array:
        if num > threeLargest[2]:  # Check if the number is larger than the smallest of the three largest
            threeLargest[0] = threeLargest[1]
            threeLargest[1] = threeLargest[2]
            threeLargest[2] = num
        elif num > threeLargest[1]:  # Check if the number is larger than the second largest
            threeLargest[0] = threeLargest[1]
            threeLargest[1] = num
        elif num > threeLargest[0]:  # Check if the number is larger than the largest
            threeLargest[0] = num
    return threeLargest
# Test cases
print(findThreeLargestNumbers([10, 5, 9, 1, 12, 15]))  # Output: [10, 12, 15]





