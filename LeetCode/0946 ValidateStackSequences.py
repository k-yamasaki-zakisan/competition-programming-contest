# https://leetcode.com/problems/validate-stack-sequences/
# Runtime: 87 ms, faster than 17.33% of Python3 online submissions for Validate Stack Sequences.
# Memory Usage: 14.4 MB, less than 82.94% of Python3 online submissions for Validate Stack Sequences.

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        from collections import deque
        stack = []
        popped = deque(popped)
        for push in pushed:
            stack.append(push)
            while len(stack) and len(popped) and stack[-1] == popped[0]:
                stack.pop()
                popped.popleft()
        return len(popped) == 0
