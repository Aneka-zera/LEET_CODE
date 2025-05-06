#https://leetcode.com/problems/container-with-most-water/submissions/1626833785/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        mh=0
        r=len(height)-1
        for i in range(0,len(height)):
            w=r-l
            h=min(height[l],height[r])*w
            mh=max(mh,h)
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return mh
