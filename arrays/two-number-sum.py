def twoNumberSum(array, targetSum):
    n = len(array)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    
    return []

result = twoNumberSum([1, 2, 3], 7)
print(result)  
