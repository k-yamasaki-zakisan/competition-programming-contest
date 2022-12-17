# https://leetcode.com/contest/weekly-contest-321/problems/remove-nodes-from-linked-list/
# 配列からListNodeを作成する

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        while head:
            if len(ans) == 0 or head.val <= ans[-1]:
                ans.append(head.val)
            else:
                while len(ans) and ans[-1] < head.val:
                    ans.pop()
                ans.append(head.val)
            head = head.next
        len_ans = len(ans)
        for i in range(len_ans - 1, -1, -1):
            if i == len_ans - 1:
                ans_link = ListNode(ans[i])
            else:
                ans_link = ListNode(ans[i], ans_link)
        return ans_link
