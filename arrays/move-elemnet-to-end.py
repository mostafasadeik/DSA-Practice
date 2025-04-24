# Arrays (Move Element to End)
# Given an array and a number, write a function that moves all instances of that number in the array to the end of the array.
# The function should perform this in place (i.e., it should not create a copy of the array) and it should do so in O(n) time complexity.
# The function should return the array after the operation.
# Sample Input
# array = [2, 1, 2, 3, 4, 2]
# toMove = 2
# Sample Output
# [1, 3, 4, 2, 2, 2]

# Approach

def moveElementToEnd(array,toMove):

    left = 0
    right = len(array) - 1

    while left < right:
        while left < right and array[right] == toMove:
            right -= 1
        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
        left +=1
    
    return array



# Test the function with different inputs

array= [2, 1, 2, 3, 4, 2]
toMove = 2
print(moveElementToEnd(array, toMove)) 