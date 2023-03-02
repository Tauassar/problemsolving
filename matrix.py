from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        while len(matrix) > 1:
            try:
                output += matrix.pop(0)
                output += [matrix[i].pop() for i in range(len(matrix))]
                output += matrix.pop()[::-1]
                output += [matrix[len(matrix) - i - 1].pop(0) for i in range(len(matrix))]
            except IndexError:
                break

        if len(matrix):
            output += matrix.pop()

        return output


matrix = [[1,2,3],[4,5,6],[7,8,9]]
res = Solution().spiralOrder(matrix=matrix)
print(res)
print([1,2,3,6,9,8,7,4,5])
