# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        mid = self.middleNode(head)
        reverseHalf = self.reverseList(mid)

        while head and reverseHalf:
            temp1 = head.next
            head.next = reverseHalf
            head = temp1
            temp2 = reverseHalf.next
            reverseHalf.next = head
            reverseHalf = temp2

        # next of tail to null
        if head:
            head.next = None

    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        # by the time fast has reached the end, the slow pointer will have covered half the distance
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # recursive method
        if not head:
            return None

        newHead = head
        
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head   # reverses the direction of the pointer, making the next node point back to the current node
        head.next = None
        
        return newHead
        