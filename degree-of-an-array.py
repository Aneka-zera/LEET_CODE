class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=defaultdict(int)
        first_occurance={}
        last_occurance={}
        for i,num in enumerate(nums):
            if num not in first_occurance:
                first_occurance[num]=i
            last_occurance[num]=i
            count[num]+=1
        degree=max(count.values())
        max_numbers=[num for num in count if count[num]==degree]
        min_length=float('inf')
        for i in max_numbers:
            length=last_occurance[i]-first_occurance[i]+1
            if length<min_length:
                min_length=length
        return min_length

