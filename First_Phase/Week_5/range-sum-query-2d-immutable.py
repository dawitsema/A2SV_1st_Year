
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix_matrix = [[]]
            return
        
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                self.prefix_matrix[i + 1][j + 1] = (
                    matrix[i][j] +
                    self.prefix_matrix[i][j + 1] +
                    self.prefix_matrix[i + 1][j] -
                    self.prefix_matrix[i][j]
                )
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.prefix_matrix:
            return 0

        return (
            self.prefix_matrix[row2 + 1][col2 + 1] -
            self.prefix_matrix[row2 + 1][col1] -
            self.prefix_matrix[row1][col2 + 1] +
            self.prefix_matrix[row1][col1]
        )

