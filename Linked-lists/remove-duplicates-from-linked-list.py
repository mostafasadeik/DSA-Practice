# Linked Lists ( Remove duplicates from linked list )
# Given a linked list, remove the duplicates from the linked list.  
# For example, given the linked list 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5,
# the function should return 1 -> 2 -> 3 -> 4 -> 5.


# Approach:

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(head):
    currentNode = head
    while currentNode is not None:
        print("currentNode:", currentNode.value)

        nextDistinctNode = currentNode.next
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next

        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode
    return head

node1 = LinkedList(1)
node2 = LinkedList(1)
node3 = LinkedList(2)
node4 = LinkedList(3)
node5 = LinkedList(3)
node6 = LinkedList(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print("Before removing duplicates:")
current = node1
while current:
    print(current.value)
    current = current.next
print("None")  

print("\nRemoving duplicates:")
removeDuplicatesFromLinkedList(node1)

print("\nAfter removing duplicates:")
current = node1
while current:
    print(current.value)
    current = current.next
print("None")  
