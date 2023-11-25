# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        pres = head
        next1 = pres.next

        while pres:
            pres.next = prev
            prev = pres
            pres = next1
            if next1:
                next1 = next1.next
        return prev
        
        