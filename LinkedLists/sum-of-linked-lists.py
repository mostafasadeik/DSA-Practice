# Write a function that returns the head of a linked list that is the sum of two other linked lists.    
# The digits are stored in reverse order, such that the 1's digit is at the head of the list


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newLinkedListHeadPointer = LinkedList(0)
    currentNode = newLinkedListHeadPointer
    carry = 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = nodeOne.value if nodeOne is not None else 0
        valueTwo = nodeTwo.value if nodeTwo is not None else 0
        sumOfValues = valueOne + valueTwo + carry

        newValue = sumOfValues % 10
        carry = sumOfValues // 10

        currentNode.next = LinkedList(newValue)
        currentNode = currentNode.next

        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None

    return newLinkedListHeadPointer.next


# -------------------------------
# Example: Invoke sumOfLinkedLists
# -------------------------------

# Make first linked list: 2 → 4 → 7  (representing 742)
a1 = LinkedList(2)
a2 = LinkedList(4)
a3 = LinkedList(7)
a1.next = a2
a2.next = a3

# Make second linked list: 9 → 4 → 5 (representing 549)
b1 = LinkedList(9)
b2 = LinkedList(4)
b3 = LinkedList(5)
b1.next = b2
b2.next = b3

# Call the function
result = sumOfLinkedLists(a1, b1)

# Print the result linked list values
print("Result LinkedList values:")
current = result
while current is not None:
    print(current.value)
    current = current.next


