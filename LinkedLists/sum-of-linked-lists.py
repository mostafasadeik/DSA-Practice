# Write a function that returns the head of a linked list that is the sum of two other linked lists.    
# The digits are stored in reverse order, such that the 1's digit is at the head of the list


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

