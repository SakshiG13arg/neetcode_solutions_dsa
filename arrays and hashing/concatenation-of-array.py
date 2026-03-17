class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # create an empty list
        ans = []
        # 2 because it has to be appended two times
        for i in range(2):
            # iterate through every number in nums
            for n in nums:
                ans.append(n)
        return ans
