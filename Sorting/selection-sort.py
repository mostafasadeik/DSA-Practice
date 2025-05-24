# Sorting (Selection Sort)
def selectionSort(array):
    # Traverse through all array elements
    for i in range(len(array)):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        array[i], array[min_index] = array[min_index], array[i]
    
    return array
# Example usage
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    sorted_arr = selectionSort(arr)
    print("Sorted array:", sorted_arr)