class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        s=[]
        for i in range(numRows):
            r=[None for _ in range(i+1)]
            r[0]=1
            r[-1]=1
            for j in range(1,len(r)-1):
                r[j]=s[i-1][j-1]+s[i-1][j]
            s.append(r)
        return s

            
        
            
