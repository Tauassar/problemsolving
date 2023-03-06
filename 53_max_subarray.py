from typing import List

from decorators import measure_execution_time


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        has_pos = False
        min_pos = None
        for num in nums:
            if num >= 0:
                has_pos = True

            if has_pos:
                if min_pos is None or 0 <= num < min_pos:
                    min_pos = num

        if not has_pos:
            return max(nums)

        seq_list = []
        prev_sum = None
        for num in nums:
            if prev_sum is None:
                if num < min_pos:
                    continue
                else:
                    prev_sum = num
            else:
                if num >= min_pos:
                    prev_sum += num
                else:
                    if prev_sum + num < 0:
                        seq_list.append(prev_sum)
                        prev_sum = 0
                    else:
                        seq_list.append(prev_sum)
                        prev_sum += num

        seq_list.append(prev_sum)

        max_sum = None
        for i in seq_list:
            if max_sum is None:
                max_sum = i
            else:
                if max_sum < i:
                    max_sum = i
        return max_sum


@measure_execution_time
def main():
    res = Solution().maxSubArray([5, 4, -1, 7, 8])
    print(f'Expected: {6}')
    print(f'Received {res}')


if __name__ == '__main__':
    main()
