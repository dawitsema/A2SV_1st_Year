class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        hashset = set()

        def backtrack(start, temp):
            val = tuple(temp.copy())
            if val not in hashset:
                hashset.add(val)
                ans.append(temp.copy())

            for i in range(start, len(nums)):
                temp.append(nums[i])
                backtrack(i + 1, temp)
                temp.pop()
            return ans

        return backtrack(0, [])