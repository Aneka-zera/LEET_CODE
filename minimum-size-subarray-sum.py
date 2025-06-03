#https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1652975538/
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        leng=float("inf")
        l=0
        
        s=0
        for r in range(len(nums)):
            s+=nums[r]
            while s>=target:
                if r-l+1<leng:
                    leng=r-l+1
                s-=nums[l]
                l+=1
        return leng if leng!=float("inf") else 0
        
