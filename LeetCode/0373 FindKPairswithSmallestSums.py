# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# Runtime: 52 ms, faster than 66.53% of Python3 online submissions for Find K Pairs with Smallest Sums.
# Memory Usage: 14.9 MB, less than 35.80% of Python3 online submissions for Find K Pairs with Smallest Sums.

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        nums1.sort()
        nums2.sort()
        ans = []
        for num1 in nums1:
            for num2 in nums2:
                if len(ans) < k:
                    heapq.heappush(ans, (-num1-num2, [num1, num2]))
                else:
                    if ans and -ans[0][0] > num1+num2:
                        heapq.heappop(ans)
                        heapq.heappush(ans, (-num1-num2, [num1, num2]))
                    else:
                        break
        return [ans[i][1] for i in range(len(ans))]
