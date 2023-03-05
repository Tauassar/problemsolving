from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        sum_grid = [[] for _ in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                vals = []
                if col > 0:
                    vals.append(
                        sum_grid[row][col-1] + grid[row][col],
                    )
                if row > 0:
                    vals.append(
                        sum_grid[row-1][col] + grid[row][col],
                    )

                if row == col == 0:
                    vals.append(grid[row][col])

                # print(f'{row = } {col = } {vals = }')
                sum_grid[row].append(min(vals))

        # print(sum_grid)
        return sum_grid[-1][-1]


print(Solution().minPathSum([[1,2,3],[4,5,6]]))
print(7)
