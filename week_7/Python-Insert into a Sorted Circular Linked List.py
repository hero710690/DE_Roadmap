class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'ListNode', insertVal: int) -> 'ListNode':
        
        if not head:
            new_node = ListNode(val=insertVal)
            new_node.next = new_node
            return new_node
        
        prev = head
        current = head.next
        
        
        while True:
            if current.val > insertVal > prev.val:
                prev.next = ListNode(val=insertVal, next=current)
                return head
            elif current.val < prev.val:
                if insertVal> current.val or insertVal< current.val:
                    prev.next = ListNode(val=insertVal, next=current)
                    return head
                
            prev, current = current, current.next
            if prev == head:
                break
        
        prev.next = ListNode(val=insertVal, next=current)
        return head
def print_circular_linked_list(head: 'ListNode'):
    if not head:
        print("The list is empty.")
        return
    
    current = head
    first = True
    while first or current != head:
        print(current.val, end=" -> ")
        current = current.next
        first = False
    print("... (back to head)")

if __name__ == '__main__':
    sol = Solution()
    node1 = ListNode(3)
    node2 = ListNode(4)
    node3 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node1  # Complete the circular link
    print_circular_linked_list(node1)
    # Insert a new value into the circular linked list
    new_head = sol.insert(node1, 0)

    print_circular_linked_list(new_head)