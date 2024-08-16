class Stack:  
    def __init__(self):  
        self.items = []  

    def push(self, item):  
        self.items.append(item)  

    def pop(self):  
        if not self.is_empty():  
            return self.items.pop()  
        return None  

    def top(self):  
        if not self.is_empty():  
            return self.items[-1]  
        return None  

    def is_empty(self):  
        return len(self.items) == 0  

    def size(self):  
        return len(self.items)  

def delete_middle(stack):  
    if stack.is_empty():  
        return  
    
    # Calculate the middle index. For 0-based index  
    size = stack.size()  
    mid_index = size // 2  

    # Helper function to delete the middle element using recursion  
    def delete_mid_util(s, current_index):  
        if current_index == mid_index:  
            s.pop()  # Removing the middle element  
            return  
        
        # Move top element to the next recursion  
        temp = s.pop()  
        delete_mid_util(s, current_index + 1)  
        
        # Push the element back after recursive call  
        s.push(temp)  

    delete_mid_util(stack, 0)  

# Example Usage  
stack = Stack()  
stack.push(1)  
stack.push(2)  
stack.push(3)  
stack.push(4)  
stack.push(5)  

print("Original Stack:", stack.items)  
delete_middle(stack)  
print("Stack after deleting the middle element:", stack.items)