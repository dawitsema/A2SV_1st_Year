class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        k = k
        def helper(x, path):
            # nonlocal k
            if k == len(path):
                ans.append(path.copy())
                return 

            for i in range(x,n+1):
                path.append(i)
                helper(i+1, path)
                path.pop()
            
        helper(1, [])
        return ans