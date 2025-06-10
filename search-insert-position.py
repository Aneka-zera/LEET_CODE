#https://leetcode.com/problems/search-insert-position/submissions/1569175878/
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        for i in range(len(nums)):
            if nums[i]>target and nums[i-1]<target:
                return i
            elif nums[0]>target:
                return 0
            elif nums[len(nums)-1]<target:
                return len(nums)
    
        
