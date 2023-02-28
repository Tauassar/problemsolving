import copy

class Solution:
    cache = {}

    def populateUnplacable(self, board, x, y):
        length = len(board)
        for i in range(length):
            for j in range(length):
                placable = True

                if (i == x and j == y) or board[i][j] == 'x' or board[i][j] == 'Q':
                    continue

                if i == x:
                    placable = False
                if j == y:
                    placable = False

                if abs(i - x) == abs(j - y):
                    placable = False

                if not placable:
                    board[i][j] = 'x'
        return board

    def solveNQueensRecursive(self, n: int, board=None) -> list[list[str]]:
        if not n:
            return board

        length = len(board)

        for i in range(length):
            for j in range(length):
                if board[i][j] == '.':
                    board[i][j] = 'Q'
                    return self.solveNQueensRecursive(
                        n - 1,
                        self.populateUnplacable(board, i, j),
                    )

    def get_indexes(self, temp_res):
        indexes = []
        for y, row_val in enumerate(temp_res):
            try:
                x = row_val.index('Q')
            except ValueError:
                continue
            else:
                indexes.append(f'{x}:{y}')
        return ';'.join(indexes)

    def save_to_cache(self, temp_res):
        self.cache[self.get_indexes(temp_res)] = True

    def set_display(self, table):
        res = []
        for row in table:
            res.append(''.join(row).replace('x', '.'))

        return res

    def solveNQueens(self, n: int, board=None) -> list[list[str]]:
        self.cache = {}

        if board is None:
            board = [['.' for _ in range(n)] for _ in range(n)]

        if not n:
            return board

        # print('board')
        # for row in board:
        #     print(row)

        res = []

        length = len(board)

        for i in range(length):
            for j in range(length):
                if board[i][j] == '.':
                    board_temp = copy.deepcopy(board)
                    board_temp[i][j] = 'Q'
                    temp_res = self.solveNQueensRecursive(
                        n - 1,
                        self.populateUnplacable(board_temp, i, j),
                    )
                    res += [self.set_display(temp_res)] if temp_res and not self.cache.get(
                        self.get_indexes(temp_res), False) else []
                    if temp_res and not self.cache.get(self.get_indexes(temp_res), False):
                        print('Round')
                        print(temp_res)
                        self.save_to_cache(temp_res)
        return res


s = Solution()

res = s.solveNQueens(5)

expected = [["Q....", "..Q..", "....Q", ".Q...", "...Q."],
            ["Q....", "...Q.", ".Q...", "....Q", "..Q.."],
            [".Q...", "...Q.", "Q....", "..Q..", "....Q"],
            [".Q...", "....Q", "..Q..", "Q....", "...Q."],
            ["..Q..", "Q....", "...Q.", ".Q...", "....Q"],
            ["..Q..", "....Q", ".Q...", "...Q.", "Q...."],
            ["...Q.", "Q....", "..Q..", "....Q", ".Q..."],
            ["...Q.", ".Q...", "....Q", "..Q..", "Q...."],
            ["....Q", ".Q...", "...Q.", "Q....", "..Q.."],
            ["....Q", "..Q..", "Q....", "...Q.", ".Q..."]]

# print(res)
# print(expected)

print(f'\n\n\nSolutions: {len(res)}')

# for sol in res:
#     print('\n\nSol')
#     for row in sol:
#         print(row)

print(f'\n\n\nExpected: {len(expected)}')

# for sol in expected:
#     print('\n\nSol')
#     for row in sol:
#         print(row)
