# Stacks ( Min Max Stack Construction )
# Write a minMaxStack class for a minMax stack.

class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = []

    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()
    
    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if self.minMaxStack:
            lastMinMax = self.minMaxStack[-1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[-1]["min"]
    
    def getMax(self):
        return self.minMaxStack[-1]["max"]

stack = MinMaxStack()

stack.push(5)
print("After push(5):")
print("Min:", stack.getMin())  # 5
print("Max:", stack.getMax())  # 5
print("Top:", stack.peek())    # 5
print()

stack.push(2)
print("After push(2):")
print("Min:", stack.getMin())  # 2
print("Max:", stack.getMax())  # 5
print("Top:", stack.peek())    # 2
print()

stack.push(8)
print("After push(8):")
print("Min:", stack.getMin())  # 2
print("Max:", stack.getMax())  # 8
print("Top:", stack.peek())    # 8
print()

popped = stack.pop()
print(f"After pop() (removed {popped}):")
print("Min:", stack.getMin())  # 2
print("Max:", stack.getMax())  # 5
print("Top:", stack.peek())    # 2
print()

popped = stack.pop()
print(f"After pop() (removed {popped}):")
print("Min:", stack.getMin())  # 5
print("Max:", stack.getMax())  # 5
print("Top:", stack.peek())    # 5
print()

