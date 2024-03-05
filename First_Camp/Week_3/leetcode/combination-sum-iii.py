class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [x for x in range(1, 10)]
        ans = []
        summ = 0
        hashset = set()
        def helper(temp, start):
            nonlocal summ
            if summ > n:
                return
            if n == summ and len(temp.copy()) == k:
                val = tuple(sorted(temp.copy()))
                if val not in hashset:
                    hashset.add(val)
                    ans.append(temp.copy())

            x = 0
            for i in range(start, len(nums)):
                if nums[i] != x:
                    summ += nums[i]
                    temp.append(nums[i])
                    helper(temp, i + 1)
                    summ -= nums[i]
                    x = temp.pop()

        helper([], 0)
        return ans