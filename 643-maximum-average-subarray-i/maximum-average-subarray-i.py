class Solution(object):
    def findMaxAverage(self, nums, k):
        window=sum(nums[:k])
        maxi=window
        for i in range (k,len(nums)):
            window=window-nums[i-k]+nums[i]
            maxi=max(maxi,window)
        return maxi/float(k)
