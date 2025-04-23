# Arrays (Non Constructible Change)
# Problem: Given an array of positive integers representing coin denominations, find the minimum amount of change that cannot be created with the given coins.
# Approach:
# 1. Sort the array of coins in ascending order.
# 2. Initialize a variable to track the current amount of change we can create.
# 3. Iterate through the sorted coins:
#    - If the current coin is greater than the current change + 1, return current change + 1.
#    - Otherwise, add the coin value to the current change.
# 4. If we finish iterating through the coins without finding a gap, return current change + 1.
# 5. Time complexity: O(n log n) for sorting, O(n) for iterating through the coins, total O(n log n).
# 6. Space complexity: O(1) since we are using a constant amount of space.

def nonConstructibleChange(coins):
    coins.sort()  # Step 1: Sort coins in ascending order
    currentChange = 0  # Step 2: Track the current amount of change we can create
    
    for coin in coins:
        if coin > currentChange + 1:
            return currentChange + 1  # Step 3: Found a gap we can't fill
        currentChange += coin  # Step 4: Extend the range of change we can create
    
    return currentChange + 1  # Step 5: If no gaps, return the next unmakeable change ____________

# Example usage
result = nonConstructibleChange([1, 2, 5])
print(result)  # Output: 4
result2 = nonConstructibleChange([5, 7, 1, 1, 2, 3, 22])



