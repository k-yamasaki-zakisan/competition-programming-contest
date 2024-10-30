class Solution {
    fun countSquares(matrix: Array<IntArray>): Int {
        val H = matrix.size
        val W = matrix.first().size
        val dp = ArrayList(List(H) { ArrayList(List(W) { 0 })})
        var ans = 0
        for (h in 0 until H) {
            for (w in 0 until W) {
                if (matrix[h][w] == 0) {
                    dp[h][w] = 0
                } else {
                    dp[h][w] = when {
                        h > 0 && w > 0 -> minOf(dp[h-1][w], dp[h-1][w-1], dp[h][w-1]) + 1
                        else -> 1
                    }
                    ans += dp[h][w]
                }
            }
        }
        return ans
    }
}