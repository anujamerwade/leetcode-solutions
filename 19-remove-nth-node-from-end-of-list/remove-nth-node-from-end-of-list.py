# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        curr = head

        while curr:
            curr = curr.next
            length += 1
        
        skip = length - n

        # here head itself would be removed so result would be everything after the head
        if skip == 0:
            return head.next

        # restore curr to head
        curr = head
        for i in range(skip-1):
            curr = curr.next
        print(curr)

        curr.next = curr.next.next
        return head