"""Example:

Input: List: 1 -> 2 -> 3 -> 5 -> 2 -> 10, Key: 2
Output: 1 -> 2 -> 3 -> 5 -> 10
Explanation: The last occurrence of 2 in the list is deleted.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteLastOccurrence(head, key):
    if not head:
        return head
    cur_node = head
    last_occurrence = None
    last_occurrence_prv_node = None
    prv_node = None
    while cur_node:
        if cur_node.val == key:
            last_occurrence = cur_node
            last_occurrence_prv_node = prv_node

        prv_node = cur_node
        cur_node = cur_node.next
    
    if last_occurrence:
        if last_occurrence == head:
            head = head.next
        elif last_occurrence_prv_node:
            last_occurrence_prv_node.next = last_occurrence.next
    return head


# Helper function to print the list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(5, ListNode(2, ListNode(10))))))
print("Original List:")
printList(head)
head = deleteLastOccurrence(head, 2)
print("After Deleting Last Occurrence of 2:")
printList(head)