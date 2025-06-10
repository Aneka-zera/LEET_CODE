#https://leetcode.com/problems/defuse-the-bomb/
class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(code)
        if k==0:
            return [0]*n
        ans=[]
        nums=code+code
        for i in range(n):
            if k>0:
                ans.append(sum(nums[i+1:i+k+1]))
            if k<0:
                ans.append(sum(nums[i+n+k:i+n]))
        return ans

