# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from decorators import measure_execution_time


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''
        longest_temp = ''
        for char in s:
            if char in longest_temp:
                longest = longest_temp if len(longest_temp) > len(longest) else longest

                while len(longest_temp):
                    longest_temp = longest_temp[1:]
                    if char not in longest_temp:
                        break

            longest_temp += char

        if len(longest_temp):
            print(longest_temp)
            longest = longest_temp if len(longest_temp) > len(longest) else longest

        return len(longest)


@measure_execution_time
def main():
    in_val = "dvdf"

    print(Solution().lengthOfLongestSubstring(in_val))
    print(3)


if __name__ == '__main__':
    main()
