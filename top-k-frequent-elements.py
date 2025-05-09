#https://leetcode.com/problems/top-k-frequent-elements/
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        b=[]
        d=dict()
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        s= sorted(d.items(), key=lambda x: x[1], reverse=True)
        keys = [key for key, value in s]
        return keys[:k]

        
        
