#https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
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
            if d[i]==1:
                return i


def singleNumber(nums):  
    result = 0  
    for num in nums:  
        result ^= num  # XOR cancels out duplicates  
    return result  
