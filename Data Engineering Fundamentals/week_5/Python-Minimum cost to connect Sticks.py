import heapq
def connectSticks(sticks):
    if len(sticks) == 0:
        return 0
    heapq.heapify(sticks)
    total = 0
    while len(sticks)>1:
        first = heapq.heappop(sticks)
        second = heapq.heappop(sticks)
        cost = first+second
        total+=cost
        heapq.heappush(sticks, cost)
    return total
if __name__ == '__main__':
    sticks = [2,4,3]
    ans = connectSticks(sticks)
    print(ans)
