class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        val = float("-inf")
        stack = []

        nums.reverse()
        for i in range(len(nums)):
            if stack and val > nums[i]:
                return True

            while stack and stack[-1] < nums[i]:
                val = max(stack.pop(), val)
            
            stack.append(nums[i])
        
        return False

        