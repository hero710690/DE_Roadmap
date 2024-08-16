# https://leetcode.com/problems/design-circular-queue/description/
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None]*k
        self.rear = -1
        self.front = 0
        self.cnt = 0
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            self.cnt+=1
            return True
    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
            self.cnt -=1
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        return -1
    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.rear]
        return -1
    def isEmpty(self) -> bool:
        return self.cnt==0

    def isFull(self) -> bool:
        return self.cnt==self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()