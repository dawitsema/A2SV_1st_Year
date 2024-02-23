class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                dictionary[stack.pop()] = num
            stack.append(num)

        ans = [-1]*len(nums1)
        for i, num in enumerate(nums1):
            if num in dictionary:
                ans[i] = dictionary[num]
        
        return ans