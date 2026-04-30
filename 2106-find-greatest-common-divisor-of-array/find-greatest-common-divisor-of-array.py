class Solution(object):
    def findGCD(self, nums):
        a = min(nums)
        b = max(nums)
        
        # Euclidean Algorithm
        while b != 0:
            a, b = b, a % b
        
        return a