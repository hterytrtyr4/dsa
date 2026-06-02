class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        ans=[]

        for num in set1:
            if num in set2:
                ans.append(num)
        return ans