# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next :
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
    

if __name__ == '__main__':
    # Example usage:
    head = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2)))
    sol = Solution()
    ans = sol.deleteDuplicates(head) #ans = 2
    print(ans)