#https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        lp=len(p)
        ls=len(s)
        if lp>ls:
            return []
        cp=Counter(p)
        cs=Counter(s[:len(p)-1])
        result=[]
        for i in range(lp-1,ls):
            cs[s[i]]+=1
            start=i-lp+1
            if cs==cp:
                result.append(start)
            cs[s[start]]-=1
            if cs[s[start]]==0:
                del cs[s[start]]
        return result
