class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(0,len(nums)):
            ls=0
            rs=0
            ls=sum(nums[0:i])
            rs=sum(nums[i+1:len(nums)])
            print(ls)
            print(rs)
            if(ls==rs):
                return i
        return -1




        
