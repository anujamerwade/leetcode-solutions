# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # total = 0
        # temp = head

        # while temp:
        #     temp = temp.next
        #     total += 1
        # middle = total//2

        # hops = 0
        # temp = head

        # while hops < middle and temp:
        #     temp = temp.next
        #     hops += 1
        # return temp

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow




        