class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j or len(mat)-1 == j+i:
                    ans += mat[i][j]
        
        return ans
        
        
        