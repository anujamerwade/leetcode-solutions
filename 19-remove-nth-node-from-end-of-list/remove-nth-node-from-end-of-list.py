# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        curr = head
        dummy = ListNode(0)
        dummy.next = head

        while curr:
            curr = curr.next
            length += 1
        
        skip = length - n

        # prev = self.get(skip, head)
        # print(prev)
        curr = dummy
        for i in range(skip):
            curr = curr.next
        print(curr)

        curr.next = curr.next.next
        return dummy.next
    
    # def get(self, idx, head):
    #     node = head
    #     for i in range(idx):
    #         node = node.next
    #     return node
