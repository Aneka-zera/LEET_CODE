#https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        av=[]
        s=sorted(nums)
        l=len(nums)
        i=0
        while(i<l/2):
            
            a=s[0]
            b=s[-1]
            del s[0]
            del s[-1]
            avg=(a+b)/2.0
            av.append(avg)
            i+=1
        return min(av)


















