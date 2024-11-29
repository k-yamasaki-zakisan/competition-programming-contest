class Solution {
    fun minimumSumSubarray(nums: List<Int>, l: Int, r: Int): Int {
        var ans = 100000000
        for (i in 0 until nums.size-l+1) {
            var tmp = 0
            for (j in i until minOf(i+r, nums.size)) {
                tmp += nums[j]
                if (l <= j-i+1 && 0 < tmp) {
                    ans = minOf(ans, tmp)
                }
            }
        }
        if (ans == 100000000) {return -1}
        return ans
    }
}