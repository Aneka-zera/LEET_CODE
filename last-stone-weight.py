#https://leetcode.com/problems/last-stone-weight/
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        mh=[-x for x in stones]
        heapq.heapify(mh)
        while len(mh)>1:
            first=-heapq.heappop(mh)
            second=-heapq.heappop(mh)
            if first!=second:
                a=first-second
                heapq.heappush(mh,-a)
        return -mh[0] if mh else 0



            
            
            
            

