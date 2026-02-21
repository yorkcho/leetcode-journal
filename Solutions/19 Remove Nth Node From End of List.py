from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # sz<=1
        if not head:
            return head

        # nth from end: Use fast and slow ptr
        # 1. Fast move n step
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast: #exception, n=sz(meaning remove head)
            return head.next
        # 2. move together til fast.next==none
        while fast.next:
            slow = slow.next
            fast = fast.next
        # 3. now slow is one before target. Remove target
        slow.next = slow.next.next
        
        return head
        