https://leetcode.com/problems/majority-element/
nums.sort()
        return nums[len(nums)/2]

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=dict()
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in nums:
            if d[i]>len(nums)//2:
                return i
        
