# Sorting (Insertion Sort)

def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j , j - 1, array)
            j -= 1
    return array

def swap(i , j, array):
    array[i], array[j] = array[j], array[i]
# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Original array:", arr)
    sorted_arr = insertionSort(arr)
    print("Sorted array:", sorted_arr)