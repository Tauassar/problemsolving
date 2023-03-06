"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"""
from typing import List

from decorators import measure_execution_time


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res


@measure_execution_time
def main():
    in_val = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(in_val))
    print(0)


if __name__ == '__main__':
    main()
