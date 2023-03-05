from typing import List


class Solution:
    cache = {}

    def recursive(self, matrix, pos_row=0, pos_col=0, obstacles=None) -> int:
        res = 0
        # print(f'{matrix = } {pos_x = } {pos_y = }')
        if obstacles is None:
            obstacles = []

        if [pos_row, pos_col] in obstacles:
            return 0

        if pos_row >= matrix[0] - 1 and pos_col >= matrix[1] - 1:
            print(obstacles)
            return 1

        if pos_row < matrix[0] - 1:
            c_row = pos_row + 1
            c_col = pos_col
            cached = self.cache.get(f'{c_row}:{c_col}', None)

            if not cached:
                res_temp = self.recursive(matrix, c_row, c_col, obstacles)
                # print(f'{c_row = } {c_col = } {res_temp = }')
                self.cache[f'{c_row}:{c_col}'] = res_temp
                res += res_temp
            else:
                # print(f'{c_row = } {c_col = } {cached = }')
                res += cached

        if pos_col < matrix[1] - 1:
            c_row = pos_row
            c_col = pos_col + 1
            cached = self.cache.get(f'{c_row}:{c_col}', None)

            if not cached:
                res_temp = self.recursive(matrix, c_row, c_col, obstacles)
                # print(f'{c_row = } {c_col = } {res_temp = }')
                self.cache[f'{c_row}:{c_col}'] = res_temp
                res += res_temp
            else:
                res += cached

        return res

    def uniquePaths(self, m: int, n: int, obstacles: List[List[int]] = None) -> int:
        if not obstacles:
            obstacles = []

        self.cache = {}
        sol = self.recursive((m, n), obstacles=obstacles)
        print(self.cache)
        return sol

    def get_obstacle_coords(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        res = []
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[row])):
                if obstacleGrid[row][col]:
                    res.append([row, col])
        print(res)
        return res

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        return self.uniquePaths(
            len(obstacleGrid),
            len(obstacleGrid[0]),
            obstacles=self.get_obstacle_coords(obstacleGrid),
        )


print(Solution().uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))
print(0)
