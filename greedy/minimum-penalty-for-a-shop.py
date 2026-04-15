class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        res = 0
        penalty = 0
        minPenalty = 0
        for i, c in enumerate(customers):
            penalty += 1 if c == "Y" else -1
            if penalty > minPenalty:
                minPenalty = penalty
                res = i + 1
        return res
