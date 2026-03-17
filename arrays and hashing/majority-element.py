class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # after sorting the numbers the maximum occuring element will come at the middle
        nums.sort()
        # prints the middle value
        return nums[len(nums) // 2]
