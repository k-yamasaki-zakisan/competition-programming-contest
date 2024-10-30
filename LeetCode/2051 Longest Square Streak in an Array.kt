class Solution {
    fun longestSquareStreak(nums: IntArray): Int {
        var longNums = nums.map { it.toLong() }
        val setNums = longNums.toSet()
        var ans = 0
        for (num in longNums) {
            var cnt = 1
            var tmpNum = num * num
            while (tmpNum in setNums) {
                cnt += 1
                tmpNum *= tmpNum
            }
            ans = maxOf(ans, cnt)
        }
        return if (ans == 1) -1 else ans
    }
}