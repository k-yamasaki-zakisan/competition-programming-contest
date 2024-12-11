class Solution {
    fun maximumBeauty(nums: IntArray, k: Int): Int {
        val maxVal = nums.max()
        val numMemo = ArrayList(List(maxVal+k+10) { 0 })
        for (num in nums) {
            numMemo[maxOf(0, num-k)] += 1
            numMemo[num+k+1] -= 1
        }
        for (i in 1 until numMemo.size) {
            numMemo[i] += numMemo[i-1]
        }
        return numMemo.max()
    }
}