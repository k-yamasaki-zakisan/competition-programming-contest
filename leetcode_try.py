from typing import List, Optional

from numpy import s_

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        dp = {0: []}

        skill_to_index_map = {skill: i for i, skill in enumerate(req_skills)}

        for index in range(len(people)):
            person_skills_bit_rep = 0
            for skill in people[index]:
                person_skills_bit_rep |= 1 << skill_to_index_map[skill]
            tasks = list(dp.keys())

            for task_i in tasks:
                new_task = task_i | person_skills_bit_rep
                if (new_task not in dp) or (len(dp[new_task]) > len(dp[task_i]) + 1):
                    dp[new_task] = dp[task_i] + [index]

        return dp[(1 << len(req_skills)) - 1]


S = Solution()
req_skills = ["gvp", "jgpzzicdvgxlfix", "kqcrfwerywbwi", "jzukdzrfgvdbrunw", "k"]
people = [
    [],
    [],
    [],
    [],
    ["jgpzzicdvgxlfix"],
    ["jgpzzicdvgxlfix", "k"],
    ["jgpzzicdvgxlfix", "kqcrfwerywbwi"],
    ["gvp"],
    ["jzukdzrfgvdbrunw"],
    ["gvp", "kqcrfwerywbwi"],
]
print(S.smallestSufficientTeam(req_skills, people))
