"""https://leetcode.com/problems/container-with-most-water/submissions/909706766/"""
from typing import List

from decorators import measure_execution_time


class Solution:
    @staticmethod
    def get_area(i, val_i, j, val_j):
        height = min(val_i, val_j)
        length = j - i
        return height * length, height, length

    def maxArea(self, height: List[int]) -> int:
        max_vol = 0

        l = 0
        r = len(height) - 1

        while l < r:

            max_vol_temp, _, _ = self.get_area(
                l, height[l], r, height[r],
            )
            if max_vol < max_vol_temp:
                max_vol = max_vol_temp

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return max_vol


@measure_execution_time
def main():
    in_val = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(in_val))
    print(49)


if __name__ == '__main__':
    main()
