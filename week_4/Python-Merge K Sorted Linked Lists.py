from typing import List, Optional
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []

        for l in lists:
            while l:
                heapq.heappush(h, l.val)
                l = l.next
        
        newLinkedList = ListNode(None)
        current = newLinkedList
        while h:
            
            val = heapq.heappop(h)
            current.next = ListNode(val)
            current = current.next
        
        return newLinkedList.next
    

    
if __name__ == '__main__':
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    sol = Solution()
    ans = sol.mergeKLists([l1,l2,l3])
    while ans:
        print(ans.val, end=" -> ")
        ans = ans.next