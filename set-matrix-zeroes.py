#https://leetcode.com/problems/set-matrix-zeroes/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        l1=len(matrix)
        l2=len(matrix[0])
        zr=set()
        zc=set()
        for i in range(l1):
            for j in range(l2):
                if matrix[i][j]==0:
                    zr.add(i)
                    zc.add(j)
        for i in range(l1):
            for j in range(l2):
                if i in zr or j in zc:
                    matrix[i][j]=0
        return matrix





        
