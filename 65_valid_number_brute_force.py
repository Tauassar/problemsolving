# https://leetcode.com/problems/valid-number/
from typing import List

from decorators import measure_execution_time


class Solution:


    def isNumber(self, s: str) -> bool:
        if 'inf' in s.lower():
            return False

        try:
            float_val = float(s)
        except ValueError:
            return False
        return True


@measure_execution_time
def main():
    in_val = "0"
    print(Solution().isNumber(in_val))
    print(0)


if __name__ == '__main__':
    main()
