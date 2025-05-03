# Linkedlists ( Remove the kth node from the end of a linked list )
# Given a linked list, remove the kth node from the end of the end of a linked list. 

# Approach:

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print_list(self):
        current = self
        while current:
            print(current.value, end=" → " if current.next else "\n")
            current = current.next

def removeKthNodeFromEnd(head, k):
    print(f"Removing {k}th node from the end.")  # Print the value of k
    counter = 1
    first = head
    second = head

    while counter <= k:
        second = second.next
        counter += 1
    
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return 
    
    while second.next is not None:
        second = second.next
        first = first.next

    first.next = first.next.next

node1 = LinkedList(1)
node2 = LinkedList(2)
node3 = LinkedList(3)
node4 = LinkedList(4)
node5 = LinkedList(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before removal:")
node1.print_list()

k = 5 
removeKthNodeFromEnd(node1, k)

print("After removal:")
node1.print_list()
