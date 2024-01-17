class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ans = [0, nums[0]]
        for i in range(1, len(nums)):
            self.ans.append(self.ans[-1] + self.nums[i])
        

    def sumRange(self, left: int, right: int) -> int:
        return self.ans[right + 1] - self.ans[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)