class Solution {
    fun findScore(nums: IntArray): Long {
        val used = mutableSetOf<Int>()
        var ans = 0L
        val n = nums.size

        val sortNums = nums.mapIndexed { index, num -> num to index }.sortedBy { it.first }

        for ((num, i) in sortNums) {
            if (i in used) continue
            ans += num
            used.add(i)
            if (0 <= i - 1) used.add(i - 1) 
            if (i + 1 < n) used.add(i + 1)
        }

        return ans
    }
}