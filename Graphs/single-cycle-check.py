# Graphs ( Single  Cycle Check ) - Check if a graph has a single cycle
# You're given an array of integers where each integer represents a jump of it's value in the array.
# Write a function that returns true if the array has a single cycle, and false otherwise.

def hasSingleCycle(array):
    if len(array) == 0:
        return False
    
    visited = 0
    currentIndex = 0
    
    while visited < len(array):
        if visited > 0 and currentIndex == 0:
            return False
        
        visited += 1
        jump = array[currentIndex]
        currentIndex = (currentIndex + jump) % len(array)
        # print(-4 % len(array))
        print(f"Visited: {visited}, Current Index: {currentIndex}, Jump: {jump}")
  
    return currentIndex == 0


# Example usage
if __name__ == "__main__":
    # Test cases
    print(hasSingleCycle([2, 3, 1, -4, -4, 2]))  # True
