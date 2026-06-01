class Solution(object):
    def minimizeArrayValue(self, nums):
      prefix=0
      maximum=0
      for i in range(len(nums)):
        prefix +=nums[i]
        maximum=max(maximum,(prefix + i)//(i+1))
      return maximum