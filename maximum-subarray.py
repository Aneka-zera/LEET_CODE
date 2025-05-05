#https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=current=nums[0]
        for num in nums[1:]:
            current=max(num,current+num)
            max_sum=max(max_sum,current)

        return max_sum
