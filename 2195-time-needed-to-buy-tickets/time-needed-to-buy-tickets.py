class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = 0
        l = len(tickets)
        while tickets[k] :
            for i in range(l) :
                if tickets[k] < 1 :
                    return t
                if tickets[i] < 1 :
                    continue
                t += 1
                tickets[i] -= 1
        return t