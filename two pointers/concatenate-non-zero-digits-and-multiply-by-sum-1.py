class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        n_sum = 0
        for i in str(n):
            digit = int(i)
            if digit != 0:
                x = x * 10 + digit
                n_sum += digit
        return x * n_sum
