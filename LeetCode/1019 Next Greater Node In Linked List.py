# https://leetcode.com/problems/next-greater-node-in-linked-list/
# Runtime: 308 ms, faster than 97.64% of Python3 online submissions for Next Greater Node In Linked List.
# Memory Usage: 19 MB, less than 43.00% of Python3 online submissions for Next Greater Node In Linked List.

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack, ans = [], []
        while head:
            while stack and ans[stack[-1]] < head.val:
                ans[stack.pop()] = head.val
            stack.append(len(ans))
            ans.append(head.val)
            head = head.next
        for i in stack:
            ans[i] = 0
        return ans
