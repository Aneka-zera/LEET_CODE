class Solution(object):
    def reverse(self, n):
        """
        :type x: int
        :rtype: int
        """
       
        is_neg = n < 0
        a = str(abs(n))
        b = a[::-1]
        c = int(b)
        if is_neg:
            c = -c
        if c < -2**31 or c > 2**31 - 1:
            return 0
        return c
            
