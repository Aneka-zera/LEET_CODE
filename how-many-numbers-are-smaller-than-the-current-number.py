#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=[]
        for i in nums:
            c=0
            for j in range(0,len(nums)):
                if i>nums[j]:
                    c+=1
            s.append(c)
        return s
