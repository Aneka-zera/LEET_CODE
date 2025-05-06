#https://leetcode.com/problems/move-zeroes/


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ind=0
        l=0
        
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[l],nums[i]=nums[i],nums[l]
                l+=1
            
            

                
        return nums

        
