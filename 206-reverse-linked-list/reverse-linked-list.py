# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# prev > pres > next1
        # 1 > 2 > 3 > 4 > 5 > null
        # null < 1 < 2 < 3 < 4 < 5
        
        # iterative method
        # if not head:
        #     return head
        # prev = None
        # pres = head
        # next1 = pres.next

        # while pres:
        #     pres.next = prev
        #     prev = pres
        #     pres = next1
        #     if next1:
        #         next1 = next1.next
        # return prev

        # recursive method
        if not head:
            return None

        newHead = head
        
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head   # reverses the direction of the pointer, making the next node point back to the current node
        head.next = None
        
        return newHead
        