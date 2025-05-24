# Recursion (Powerset)
# Write a function that takes in an array of unique integers and returns its powerset.
# The powerset of a set is the set of all its subsets, including the empty set and the set itself.

def powerset(array, index=0):
    if index == len(array):
        return [[]]  # Base case: return a list containing the empty set

    # Recursive call to get the powerset of the remaining elements
    subsets = powerset(array, index + 1)

    # Create new subsets by adding the current element to each of the existing subsets
    current_element = array[index]
    new_subsets = [subset + [current_element] for subset in subsets]

    # Combine the existing subsets with the new subsets
    return subsets + new_subsets

# Test cases
print(powerset([1, 2]))  # Output: [[], [2], [1], [1, 2]]