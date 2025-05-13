#https://leetcode.com/problems/group-anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for w in strs:
            sw=''.join(sorted(w))
            if sw not in d:
                d[sw]=[]
            d[sw].append(w)
        return list(d.values())
