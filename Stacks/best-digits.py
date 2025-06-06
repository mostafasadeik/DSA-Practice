# Stacks (Best Digits)
# Write a function that takes in a number as a string and returns the best digits of that number.


# The best digits of a number are the digits that can be obtained by removing a certain number of digits from the number

def bestDigits(number,numDigits):
    stack = []

    for digit in number:
        while numDigits > 0 and len(stack) > 0 and digit > stack[-1]:
            numDigits -= 1
            stack.pop()
        stack.append(digit)
    while numDigits > 0:
        numDigits -= 1
        stack.pop()

    return "".join(stack)        
