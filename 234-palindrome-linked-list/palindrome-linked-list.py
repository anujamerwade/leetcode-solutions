# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # get mid of linkedlist
        mid = self.middleNode(head)

        # reverse the linkedlist from mid to end
        reversedHalf = self.reverseList(mid)
        rereverseHead = reversedHalf

        # compare head and mid
        while head and reversedHalf:
            if head.val != reversedHalf.val:
                break   # because we want to rereverse it
            head = head.next
            reversedHalf = reversedHalf.next
        
        self.reverseList(rereverseHead)

        # if we reach here without the break condition
        return not head or not reversedHalf

        
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        # by the time fast has reached the end, the slow pointer will have covered half the distance
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# prev > pres > next1
        # 1 > 2 > 3 > 4 > 5 > null
        # null < 1 < 2 < 3 < 4 < 5
        
        # iterative method
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