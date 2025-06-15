#https://leetcode.com/problems/pascals-triangle/
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        pr=self.generate(numRows-1)
        nr=[1]*numRows
        for i in range(1, numRows - 1):
            nr[i] = pr[-1][i - 1] + pr[-1][i]
        
        pr.append(nr)
        return pr
