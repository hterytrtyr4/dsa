class Solution(object):
    def findDuplicate(self, nums):
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            else:
                seen.add(nums[i])