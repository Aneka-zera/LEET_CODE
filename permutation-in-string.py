#https://leetcode.com/problems/permutation-in-string/
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len1, len2 = len(s1), len(s2)
        
        if len1 > len2:
            return False
        
        # Initialize frequency maps for s1 and the sliding window in s2
        s1_count = defaultdict(int)
        window_count = defaultdict(int)
        
        # Populate initial frequency counts
        for i in range(len1):
            s1_count[s1[i]] += 1
            window_count[s2[i]] += 1
        
        # Check initial window
        if s1_count == window_count:
            return True
        
        # Slide the window through s2
        for i in range(len1, len2):
            # Remove the leftmost character of the previous window
            left_char = s2[i - len1]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1
            
            # Add the new right character
            right_char = s2[i]
            window_count[right_char] += 1
            
            # Compare frequency maps
            if s1_count == window_count:
                return True
        
        return False
