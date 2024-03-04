class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        summ = 0
        hashset = set()
        def helper(temp):
            nonlocal summ
            if summ > target:
                return
            if summ == target:
                val = tuple(sorted(temp.copy()))
                if val not in hashset:
                    hashset.add(val)
                    ans.append(temp.copy())
                
            for i in range(len(candidates)):
                summ += candidates[i]
                temp.append(candidates[i])
                helper(temp)
                summ -= candidates[i]
                temp.pop()

        helper([])
        return ans
                