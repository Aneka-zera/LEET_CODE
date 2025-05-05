https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left=maxl=0
        c_s=set()
        for r in range(len(s)):
            while s[r] in c_s:
                c_s.remove(s[left])
                left+=1
            c_s.add(s[r])
            maxl=max(maxl,r-left+1)
        return maxl





        
