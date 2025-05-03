https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=len(nums)
        ind=1
        b=nums[0]
        
        for i in range(1,a):
            if nums[i]!=b:
                nums[ind]=nums[i]
                ind+=1
                b=nums[i]
        return ind




                    

