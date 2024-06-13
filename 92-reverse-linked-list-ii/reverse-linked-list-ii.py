# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        prev = None
        curr = head

        i = 0

        while i < left-1 and curr:
            prev = curr
            curr = curr.next
            i += 1

        last = prev
        newEnd = curr
        next1 = curr.next

        j = 0
        while j < right - left + 1 and curr:
            # iterative method
            # curr.next = prev
            # prev = curr
            # curr = next1
            # if next1:
            #     next1 = next1.next
            next_node = curr.next
            curr.next = prev 
            prev = curr
            curr = next_node

            j += 1
        
        if last:
            last.next = prev
        else:
            head = prev
        
        newEnd.next = curr
        return head
        