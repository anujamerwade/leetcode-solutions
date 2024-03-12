# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        currSum = 0
        sumHash = {currSum: dummy}

        while head:
            currSum += head.val
            if currSum in sumHash:
                # remove entries
                toRemove = sumHash.get(currSum).next
                sum1 = currSum
                while(toRemove != head):
                    sum1 += toRemove.val
                    del sumHash[sum1]
                    toRemove = toRemove.next
                # draw link
                sumHash.get(currSum).next = head.next
                
            else:
                sumHash[currSum] = head
            head = head.next

        return dummy.next