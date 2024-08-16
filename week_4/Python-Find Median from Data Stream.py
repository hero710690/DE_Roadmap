#https://leetcode.com/problems/find-median-from-data-stream/description/
import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, -num))
        else:
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, num))
    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.max_heap[0]-self.min_heap[0])/2
        else:
            return float(self.max_heap[0])

if __name__ == '__main__':
    # Your MedianFinder object will be instantiated and called as such:
    
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    param_2 = obj.findMedian()
    print(param_2)
    obj.addNum(3)
    param_2 = obj.findMedian()
    print(param_2)
    obj.addNum(10)
    param_2 = obj.findMedian()
    print(param_2)
    