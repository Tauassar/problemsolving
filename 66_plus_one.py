from typing import List

from decorators import measure_execution_time


class Solution:

    @staticmethod
    def list_to_int(digits) -> int:
        int_val = 0
        ln = len(digits) - 1
        for digit in digits:
            int_val += 10 ** ln * digit
            ln -= 1

        return int_val

    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str((self.list_to_int(digits) + 1))))


@measure_execution_time
def main():
    in_val = {
        'digits': [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3],
    }

    print(Solution().plusOne(**in_val))


if __name__ == '__main__':
    main()
