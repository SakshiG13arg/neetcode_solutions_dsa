class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0
        total = 0
        for arrival, order in customers:
            t = max(t, arrival) + order
            total += t - arrival
        return total / len(customers)
