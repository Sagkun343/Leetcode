class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        s = 0
        t= 0
        f = tickets[k]
        d = len(tickets)
        for i in range(d):
            if tickets[i] < f:
                t += f - tickets[i]
        for i in range(k+1, d):
            if tickets[i] >= f:
                s += 1
        x = (f * d) - t - s
        return x