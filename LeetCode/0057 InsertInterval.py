# https://leetcode.com/problems/insert-interval/
# Runtime: 76 ms, faster than 85.28% of Python3 online submissions for Insert Interval.
# Memory Usage: 17.5 MB, less than 57.68% of Python3 online submissions for Insert Interval.

class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        if len(intervals) == 0 \
                or (newInterval[0] <= intervals[0][0] and intervals[-1][1] <= newInterval[1]):
            return [newInterval]
        matagi_flag = False
        ans = []
        m_head, m_tail = newInterval
        if m_tail < intervals[0][0]:
            ans.append(newInterval)
        for i, headtail in enumerate(intervals):
            head, tail = headtail
            if matagi_flag:
                if m_tail < head:
                    matagi_flag = False
                    ans.append([tmp_head, max(intervals[i-1][1], m_tail)])
                    ans.append([head, tail])
            else:
                if head <= m_head <= tail or head <= m_tail <= tail:
                    matagi_flag = True
                    tmp_head = min(head, m_head)
                elif m_head <= head and tail <= m_tail:
                    matagi_flag = True
                    tmp_head = min(head, m_head)
                elif 0 < i and intervals[i-1][1] < m_head and m_tail < head:
                    ans.append(newInterval)
                    ans.append([head, tail])
                else:
                    ans.append([head, tail])
        if matagi_flag:
            ans.append([tmp_head, max(intervals[-1][1], m_tail)])
        if intervals[-1][-1] < m_head:
            ans.append(newInterval)
        return ans
