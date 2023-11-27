# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k <= 0:
            return head

        length = 1

        rotate = 0
        last = head

        # find last node of the LL
        while last.next:
            last = last.next
            length += 1

        last.next = head
        rotations = k % length

        # nodes to skip
        skip = length - rotations
        newLast = head

        for i in range(skip-1):
            newLast = newLast.next
            print(newLast)
        
        head = newLast.next
        newLast.next = None

        return head

