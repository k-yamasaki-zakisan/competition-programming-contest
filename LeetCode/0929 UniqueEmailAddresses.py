# https://leetcode.com/problems/unique-email-addresses/
# Runtime: 44 ms, faster than 94.53% of Python3 online submissions for Unique Email Addresses.
# Memory Usage: 14.5 MB, less than 31.94% of Python3 online submissions for Unique Email Addresses.

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        memo = set()
        for email in emails:
            email = email.split('@')
            local = email[0]
            locals = local.split('+')
            if 1 < len(locals):
                local = locals[0]
            local = local.replace('.', '')
            domain = email[-1]
            memo.add(local+'@'+domain)
        print(memo)
        return len(memo)
