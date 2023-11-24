# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        # if head is given for a LL then use head for all the logic

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
            if fast == slow:
                # cycle is present
                slow = head

                while fast != slow:
                    fast = fast.next
                    slow = slow.next

                return slow

        return None
        