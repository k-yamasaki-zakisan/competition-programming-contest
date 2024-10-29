fun main() {
    val MAX_TIME = 1440
    val N = readLine()!!.trim().toInt()
    val TD = List(N) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    val TDSort = TD.sortedBy { it[1] }
    val dp = ArrayList(List(N+1) { ArrayList(List(MAX_TIME+1) { -1 }) })
    dp[0][0] = 0
    for (h in 0 until N) {
        val (t, d) = TDSort[h]
        for (w in 0 .. MAX_TIME) {
            if (dp[h][w] != -1 && w+t <= d) {
                dp[h+1][w+t] = maxOf(dp[h+1][w+t], dp[h][w]+1)
            }
            dp[h+1][w] = maxOf(dp[h+1][w], dp[h][w])
        }
    }
    println(dp.last().max())
}