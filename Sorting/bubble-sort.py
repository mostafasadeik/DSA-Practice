# Sorting (Bubble Sort)
# Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the
# list is repeated until the list is sorted. The algorithm gets its name from the way larger elements "bubble" to the top of the list.

# Approach: 
# 1. Start at the beginning of the list.
# 2. Compare the first two elements.
# 3. If the first element is greater than the second, swap them.
# 4. Move to the next pair of elements and repeat the process.

def bubbleSort(array):
    isSorted = False
    n = len(array)
    while not isSorted:
        isSorted = True
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False
    return array

arr =  [11, 12, 22, 25, 34, 64, 90]
print("Sorted array:", arr)

# Time Complexity: O(n^2) in the worst case, O(n) in the best case (when the array is already sorted).