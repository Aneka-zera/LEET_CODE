class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''stack = []
        next_greater = {}
        
        # Process nums2 using a monotonic decreasing stack
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # Assign -1 for elements that don't have a greater element
        for num in stack:
            next_greater[num] = -1
        
        # Map results for nums1 based on precomputed next greater values
        return [next_greater[num] for num in nums1]
        '''
        stack=[]
        nextg={}
        for num in nums2:
            while(stack and stack[-1]<num):
                nextg[stack.pop()]=num
            stack.append(num)

        for num in stack:
            nextg[num]=-1
        return [nextg[num] for num in nums1]
