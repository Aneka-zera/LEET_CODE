#https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for idx, char in enumerate(s):
            if d[char] == 1:
                return idx

        return -1
                        


                        

