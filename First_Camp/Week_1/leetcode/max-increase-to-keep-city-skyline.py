class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = [0]*len(grid)
        colMax = [0]*len(grid[0])
        past_sum = 0

        for i in range(len(grid)):
            rowMax[i] = max(grid[i])
            for j in range(len(grid[0])):
                colMax[j] = max(grid[i][j], colMax[j])
                past_sum += grid[i][j]

        present_sum = 0
        for i in range(len(rowMax)):
            for j in range(len(colMax)):
                present_sum += min(rowMax[i], colMax[j])

        return present_sum - past_sum



                

        