# https://leetcode.com/problems/text-justification/
import math
from typing import List

from decorators import measure_execution_time


class Solution:
    maxWidth: int

    def append_to_output(self, temp_arr, temp_len, out):
        if len(temp_arr) > 1:
            spaces = math.floor((self.maxWidth - temp_len) / (len(temp_arr) - 1))
            extra_spaces = (self.maxWidth - temp_len) % (len(temp_arr) - 1)
        else:
            spaces = self.maxWidth - len(temp_arr[0])
            extra_spaces = 0

        temp_str = ''
        for i, temp_word in enumerate(temp_arr):
            spaces_len = spaces
            if extra_spaces:
                spaces_len += 1
                extra_spaces -= 1

            elif i >= len(temp_arr) - 1:
                spaces_len = 0

            if len(temp_arr) == 1:
                spaces_len = spaces

            temp_str += temp_word
            temp_str += ' ' * spaces_len
        out.append(
            temp_str,
        )

    def append_last_word_to_output(self, temp_arr, out, *args, **kwargs):
        temp_str = ' '.join(temp_arr)
        temp_str += ' ' * (self.maxWidth-len(temp_str))
        out.append(
            temp_str,
        )

    def fullJustify(self, words: List[str], maxWidth: int = 16) -> List[str]:
        out = []
        temp_arr = []
        temp_len = 0
        self.maxWidth = maxWidth
        for i, word in enumerate(words):

            if len(word) + temp_len + len(temp_arr) <= self.maxWidth:
                temp_arr.append(word)
                temp_len += len(word)

            else:
                self.append_to_output(temp_arr, temp_len, out)
                temp_arr = [word]
                temp_len = len(word)

        if temp_arr:
            self.append_last_word_to_output(temp_arr, out, temp_len)

        return out


def print_res(string_arr):
    print('[')
    for str in string_arr:
        print(f'\t{str}: {len(str)}')
    print(']')


@measure_execution_time
def main():
    in_val = {
        'words': ["What","must","be","acknowledgment","shall","be"],
        'maxWidth': 16,
    }
    out = Solution().fullJustify(**in_val)
    print_res(out)
    expected_res = ["What   must   be","acknowledgment  ","shall be        "]

    print_res(expected_res)


if __name__ == '__main__':
    main()
