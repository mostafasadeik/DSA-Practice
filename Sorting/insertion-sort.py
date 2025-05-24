# Sorting (Insertion Sort)

def insertionSort(array):
    # Traverse through 1 to len(array)
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        # Move elements of array[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Original array:", arr)
    sorted_arr = insertionSort(arr)
    print("Sorted array:", sorted_arr)