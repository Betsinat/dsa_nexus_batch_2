class Solution(object):
    def getConcatenation(self, nums):
        an = nums[:]
        nums.extend(an)
        return nums
