# Searching (Binary Search)
# Binary Search is an efficient algorithm for finding an item from a sorted list of items.
# It works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.       

# Approach:

def binarySearch(array, target):
    left, right = 0, len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == target:
            return mid 
        elif array[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  
            
    return -1 