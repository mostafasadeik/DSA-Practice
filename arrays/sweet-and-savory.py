# Arrays (Sweet and Savory)
# You're hosting an event at a food festival and want to showcase the best possible paring of two dishes from the festival that complement each other.

# Input dishes = [ -3 , -5, 1, 7 ]
# Target = 8

# Output = [-3,7]
# Explanation: The dish with a taste value of -3 and the dish with a taste value of 7 together have a total taste value of 4, which is the closest to the target of 8.
# Approach:
# 1. Initialize an empty list to store the pairs of dishes.
# 2. Sort the input list of dishes in ascending order.
# 3. Initialize two pointers, one at the beginning of the list and one at the end.
# 4. While the left pointer is less than the right pointer:
#    a. Calculate the sum of the two dishes at the left and right pointers.
#    b. If the sum is equal to the target, return the pair.             
#    c. If the sum is less than the target, move the left pointer to the right.
#    d. If the sum is greater than the target, move the right pointer to the left.
# 5. If no pair is found, return an empty list.

def sweetAndSavory(dishes, target):
    sweetDishes = sorted([dish for dish in dishes if dish < 0], key=abs)
    savoryDishes = sorted([dish for dish in dishes if dish > 0])

    bestPair = [0, 0]
    bestDifference = float('inf')
    sweetIndex, savoryIndex = 0, 0

    while sweetIndex < len(sweetDishes) and savoryIndex < len(savoryDishes):
        currentSum = sweetDishes[sweetIndex] + savoryDishes[savoryIndex]

        if currentSum <= target:
            currentDifference = target - currentSum
            if currentDifference < bestDifference:
                bestDifference = currentDifference
                bestPair = [sweetDishes[sweetIndex], savoryDishes[savoryIndex]]
            savoryIndex += 1 
        else:
            sweetIndex += 1  

    return bestPair

# ✅ تجربة
dishes = [-3, -5, 1, 7]
target = 8
pair = sweetAndSavory(dishes, target)

print("Best Pair: ", pair)


