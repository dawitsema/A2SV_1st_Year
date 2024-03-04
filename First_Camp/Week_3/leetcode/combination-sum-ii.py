class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        summ = 0
        hashset = set()
        def helper(temp, start):
            nonlocal summ
            if summ > target:
                return
            
            if target == summ:
                val = tuple(sorted(temp.copy()))
                if val not in hashset:
                    hashset.add(val)
                    ans.append(temp.copy())
            x = 0
            for i in range(start, len(candidates)):
                if candidates[i] != x:
                    summ += candidates[i]
                    temp.append(candidates[i])
                    helper(temp, i + 1)
                    summ -= candidates[i]
                    x = temp.pop()
                        
                    

        helper([], 0)
        return ans