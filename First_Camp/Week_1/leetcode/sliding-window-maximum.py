class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queque = deque()
        ans = []
        for i in range(k):
            while queque and nums[queque[-1]]< nums[i]:
                queque.pop()
            queque.append(i)

        ans.append(nums[queque[0]])
        for i in range(k, len(nums)):
            while queque and nums[queque[-1]]< nums[i]:
                queque.pop()
            queque.append(i)
            while queque and i - queque[0] >= k:
                queque.popleft()
            ans.append(nums[queque[0]])

        return ans
            
            
            


