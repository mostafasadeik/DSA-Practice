# Linkedlists ( Find the middle node of a linked list )
# Given a linked list, find the middle node of the linked list.
# For example, given the linked list 1 -> 2 -> 3 -> 4 -> 5,
# the function should return the node with value 3.

# Approach:


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(head):

    slowNode = head
    fastNode= head

    while fastNode is not None and fastNode.next is not None:
        slowNode = slowNode.next
        fastNode = fastNode.next.next
    return slowNode



head = LinkedList(1)
head.next = LinkedList(2)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(5)
head.next.next.next.next.next = LinkedList(5)

middle = middleNode(head)
print(middle.value) 
