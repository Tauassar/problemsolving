from typing import Optional

from decorators import measure_execution_time


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        vals = [self]
        tail = self
        while True:
            if tail.next:
                tail = tail.next
                vals.append(tail)
            else:
                break
        return str([i.val for i in vals])


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail = head
        rotate_list = [head]

        if not k:
            return head
        elif not head:
            return head

        while True:
            if tail.next:
                tail = tail.next
                rotate_list.append(tail)
            else:
                break

        if len(rotate_list) <= 1:
            return rotate_list[0]
        else:
            k_final = k % len(rotate_list)
            # print(k_final)

        for _ in range(k_final):
            temp = rotate_list.pop()
            rotate_list[-1].next = None
            temp.next = rotate_list[0]
            rotate_list.insert(0, temp)

        return rotate_list[0]


@measure_execution_time
def main():
    vals = []
    for i in [1, 2, 3][::-1]:
        prev = None if not len(vals) else vals[-1]
        vals.append(ListNode(i, prev))

    print([i.val for i in vals[::-1]])

    print(Solution().rotateRight(vals[-1], 2000000000))


if __name__ == '__main__':
    main()
