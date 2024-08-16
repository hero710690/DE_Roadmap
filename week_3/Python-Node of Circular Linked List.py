class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_node_in_circular_linked_list(head, target):
    if not head:
        return None
    
    current = head
    visited = head  # Start the loop with the head node
    while True:
        if current.value == target:
            return current
        current = current.next
        if current == visited:
            break
        
    return None


if __name__ == '__main__':
    # Example Usage:
# Creating a circular linked list: 1 -> 2 -> 3 -> 4 -> back to 1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1  # Making the list circular

    # Example 1:
    found_node = find_node_in_circular_linked_list(node1, 3)
    print(found_node.value if found_node else "Not Found")  # Output: 3

    # Example 2:
    found_node = find_node_in_circular_linked_list(node1, 5)
    print(found_node.value if found_node else "Not Found")  # Output: Not Found