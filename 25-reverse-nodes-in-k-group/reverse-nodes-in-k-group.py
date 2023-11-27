# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k < 2 or not head:
            return head

        prev = None
        curr = head

        n = self.length(head)
        count = n//k
        while count > 0:
            last = prev
            newEnd = curr
            next1 = curr.next

            j = 0
            while j < k and curr:
                # iterative method
                curr.next = prev
                prev = curr
                curr = next1
                if next1:
                    next1 = next1.next
                
                j += 1
            
            if last:
                last.next = prev
            else:
                head = prev
            
            newEnd.next = curr
            prev = newEnd

            if not curr:
                break

            count -= 1
            
        return head
    
    def length(self, head):
        length = 0

        while head:
            head = head.next
            length += 1
        return length


        
        