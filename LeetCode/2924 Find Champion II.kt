class Solution {
    fun findChampion(n: Int, edges: Array<IntArray>): Int {
        val memo = MutableList(n) { 0 }
        for ((f, t) in edges) {
            memo[t] += 1
        }

        if (memo.count { it == 0 } != 1) return -1
        return memo.indexOf(0)
    }
}