"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res


import time

start_time = time.time()

in_val = [7,6,4,3,1]

print(Solution().maxProfit(in_val))
print(0)

print("--- %s seconds ---" % (time.time() - start_time))
