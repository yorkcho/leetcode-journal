from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right :
            return head

        dummy = ListNode(0, head)
        start = dummy
        #move to left-1
        for _ in range(left-1):
            start = start.next
        # switch
        curr = start.next
        for _ in range(right-left):
            temp = curr.next
            curr.next = temp.next
            temp.next = start.next
            start.next = temp

        return dummy.next