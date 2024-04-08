class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = 0
        l = len(tickets)
        i = 0
        while tickets[k] > 0:
            for i in range(l):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    t += 1
                    if tickets[i] == 0 and i == k:
                        return t              
            
        return t