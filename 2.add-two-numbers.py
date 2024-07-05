# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t=0
        current=l2
        current1=l1

        current.val += current1.val+t
        current1=current1.next

        [t,current.val]=divmod(current.val,10)

        while current.next is not None:
            current = current.next
            if current1 is not None:
                current.val += current1.val+t
                current1=current1.next
            else:
                current.val += t

            [t,current.val]=divmod(current.val,10)



        while t:
            if current1 is not None:
                
                [t,va] = divmod(current1.val+t,10)
                current.next = ListNode(va)
                current = current.next
                current1=current1.next
            else:
                current.next = ListNode(1)
                return l2


        current.next=current1

        return l2