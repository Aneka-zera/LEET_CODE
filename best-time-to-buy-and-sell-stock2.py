class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        r=0
        p=0
        l=0
        maxp=0
        while r<len(prices):
            if prices[l]<prices[r]:
                p=prices[r]-prices[l]
                maxp=max(maxp,p)
            else:
                l=r
            r+=1
        return maxp
