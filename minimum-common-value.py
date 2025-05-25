#https://leetcode.com/problems/minimum-common-value/
class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        l1=0
        l2=0
        len1, len2 = len(nums1), len(nums2)
        
        while l1 < len1 and l2 < len2:
            if nums1[l1]==nums2[l2]:
                return nums1[l1]
            elif nums1[l1]>nums2[l2]:
                l2+=1
            else:
                l1+=1
        return -1    
        
    

