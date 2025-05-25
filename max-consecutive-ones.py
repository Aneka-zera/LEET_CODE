https://leetcode.com/problems/max-consecutive-ones/
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=[]
        c=0
        
        for i in range(0,len(nums)-1):
            
            
            if nums[i]==1 :
                c+=1
                
            elif nums[i]==0:
                d.append(c)
                c=0
            
        if nums[-1]==1:
            c+=1
            d.append(c)
        if nums[-1]==0:
            d.append(c)
         

        if d:
            return max(d)
        else:
            return 0
        
