#https://leetcode.com/problems/single-number-ii/submissions/1659646374/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=dict()
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in nums:
            if d[i]==1:
                return i        
                
        
