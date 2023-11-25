# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print("Current head value:", head.val if head else None)  # Add this line

        if not head or not head.next:
            return head
        
        mid = self.middleNode(head)
        # print("mid", mid)
        right = self.sortList(mid)
        # print(mid)
        left = self.sortList(head)
        # print(left)
        
        return self.mergeTwoLists(left, right)

    
    def mergeTwoLists(self, list1, list2):

        ans = ListNode()
        tail = ans
        # now both point to the same listnode

        while (list1 and list2):
            if list1.val < list2.val:
                tail.next = list1   # the next node after the current tail should be the current node from list1.
                list1 = list1.next
            else:
                tail.next = list2   # the next node after the current tail should be the current node from list2.
                list2 = list2.next
            tail = tail.next    # update tail node to point to the last appended node

        if list1:
            tail.next = list1
           
        elif list2:
            tail.next = list2

        return ans.next # ans is empty but ans.text has the entire merged list now
    
    def middleNode(self, head):
        midprev = None

        # by the time fast has reached the end, the slow pointer will have covered half the distance
        while head and head.next:
            if midprev == None:
                midprev = head
            else:
                midprev = midprev.next
            head = head.next.next
        
        mid = midprev.next
        midprev.next = None
        return mid

        return slow