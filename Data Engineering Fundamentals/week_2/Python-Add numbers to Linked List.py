# Suppose you are tasked with creating a function to add a new number to a singly linked list. The challenge includes the following operations:

# Adding to the End: Append a new number to the end of the linked list.
# Adding to the Beginning: Insert a new number at the start of the linked list.
# Adding After a Given Node: Insert a new number immediately after a specified node in the list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        newNode = ListNode(value=val)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    def prepend(self, val):
        newNode = ListNode(value=val, next=self.head)
        self.head = newNode

    def insetAfter(self, prev_node, val):
        if not prev_node:
            print("Previous node is not in the list.")
            return
        newNode = ListNode(value=val)
        newNode.next = prev_node.next
        prev_node.next = newNode
        
# Example usage:
llist = LinkedList()
llist.append(3)
llist.append(4)
llist.prepend(1)
llist.insetAfter(llist.head.next, 2)  # Inserting 2 after the first node

# Function to print list
def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

print_list(llist.head)