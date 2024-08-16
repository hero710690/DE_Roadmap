# https://leetcode.com/problems/design-linked-list/
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):  
        self.head = None  

    def get(self, index):  
        if index < 0:  
            return -1  
        current = self.head  
        for _ in range(index):  
            if current is None:  
                return -1  
            current = current.next  
        return current.val if current else -1  

    def addAtHead(self, val):  
        new_node = Node(val)  
        new_node.next = self.head  
        self.head = new_node  

    def addAtTail(self, val):  
        new_node = Node(val)  
        if not self.head:  
            self.head = new_node  
            return  
        current = self.head  
        while current.next:  
            current = current.next  
        current.next = new_node  

    def addAtIndex(self, index, val):  
        if index < 0:  
            return  
        if index == 0:  
            self.addAtHead(val)  
            return  
        new_node = Node(val)  
        current = self.head  
        for _ in range(index - 1):  
            if current is None:  
                return  
            current = current.next  
        if current is None:  
            return  
        new_node.next = current.next  
        current.next = new_node  

    def deleteAtIndex(self, index):  
        if index < 0:  
            return  
        if index == 0:  
            self.head = self.head.next  
            return  
        current = self.head  
        for _ in range(index - 1):  
            if current is None:  
                return  
            current = current.next  
        if current is None or current.next is None:  
            return  
        current.next = current.next.next  
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)