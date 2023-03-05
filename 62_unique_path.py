class Solution:
    cache = {}

    def recursive(self, matrix, pos_row=0, pos_col=0) -> int:
        res = 0
        # print(f'{matrix = } {pos_x = } {pos_y = }')
        if pos_row >= matrix[0]-1 or pos_col >= matrix[1]-1:
            return 1

        if pos_row < matrix[0]-1:
            c_row = pos_row + 1
            c_col = pos_col
            cached = self.cache.get(f'{c_row}:{c_col}', None)

            if not cached:
                res_temp = self.recursive(matrix, c_row, c_col)
                # print(f'{c_row = } {c_col = } {res_temp = }')
                self.cache[f'{c_row}:{c_col}'] = res_temp
                res += res_temp
            else:
                # print(f'{c_row = } {c_col = } {cached = }')
                res += cached

        if pos_col < matrix[1]-1:
            c_row = pos_row
            c_col = pos_col + 1
            cached = self.cache.get(f'{c_row}:{c_col}', None)

            if not cached:
                res_temp = self.recursive(matrix, c_row, c_col)
                # print(f'{c_row = } {c_col = } {res_temp = }')
                self.cache[f'{c_row}:{c_col}'] = res_temp
                res += res_temp
            else:
                res += cached

        return res

    def uniquePaths(self, m: int, n: int) -> int:
        self.cache = {}
        sol = self.recursive((m, n))
        # print(self.cache)
        return sol


print(Solution().uniquePaths(m = 3, n = 7))
print(28)
