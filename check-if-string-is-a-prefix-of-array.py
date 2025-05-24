#https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/
class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        
        l=0
        r=0
        for i in words:
            a=len(i)
            
            r=r+a
            w=s[l:r]
            l=r

            if w!=i:
                return False

            if r>len(s):
                return False 
            if r==len(s):
                return True         
        return r==len(s)          


'''
b=""
        for i in words:
            b=b+i
            if b==s:
                return True
            if len(s)<len(b):
                return False
        return False         
'''
