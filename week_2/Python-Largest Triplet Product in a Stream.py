import heapq

class LargestTripletProduct:
    def __init__(self):
        # Initialize a min-heap to store the top 3 largest values
        self.heap = []
    
    def add(self, num):
        # Add new number to the heap
        heapq.heappush(self.heap, num)
        # If there are more than 3 elements, remove the smallest
        if len(self.heap) > 3:
            heapq.heappop(self.heap)
        # Calculate the product of the three largest elements
        if len(self.heap) == 3:
            return self.heap[0] * self.heap[1] * self.heap[2]
        else:
            return -1# Not enough elements to calculate the triplet product

# Example Usage
ltp = LargestTripletProduct()
stream = [1, 2, 6, 4, 5]  # Example stream of numbers
results = []
for number in stream:
    result = ltp.add(number)
    results.append(result)

print("Triplet products as numbers come in:", results)
