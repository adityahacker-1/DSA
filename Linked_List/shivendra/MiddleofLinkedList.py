from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Code starts here:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
