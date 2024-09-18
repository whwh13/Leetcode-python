from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        ans = head
        front = head 
        while n:
            n-=1
            front = front.next
        if front is None:
            ans=ans.next
            return ans

        while front.next:
            front = front.next
            head = head.next

        head.next = head.next.next

        return ans
