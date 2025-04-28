# Arrays (Best Seat)
# You walk into a movie theater and see a row of empty seats. You want to find the best seat in the row, which is defined as the seat that is furthest from the nearest occupied seat. If there are no occupied seats, the best seat is the middle seat. If there are two middle seats, choose the one with the lower index.
# Write a function that takes a list of integers representing the seats in the row, where 0 represents an empty seat and 1 represents an occupied seat. The function should return the index of the best seat.
# Example:
# Input: [1, 0, 1, 0, 0, 0, 1]


# Approach:

def bestSeat(seats):
    bestSeat = -1
    maxSpace=0

    left = 0 
    while left < len(seats):
        right = left + 1
        while right < len(seats) and seats[right] == 0:
            right +=1 

        availableSpace = right - left - 1 
        if availableSpace > maxSpace:
            bestSeat = (left + right) // 2
            maxSpace = availableSpace
        left = right 
        
    return bestSeat

# usage

result = bestSeat(seats=[1, 0, 1, 0, 0, 0, 1])
print(result)  # Output: 3