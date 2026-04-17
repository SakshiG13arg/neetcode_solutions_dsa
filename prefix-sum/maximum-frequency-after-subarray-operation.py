class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        countK = nums.count(k)
        res = 0
        for i in range(1, 51):
            if i == k:
                continue
            count = 0
            for num in nums:
                if num == i:
                    count += 1
                if num == k:
                    count -= 1
                count = max(count, 0)
                res = max(res, countK + count)
        return res
