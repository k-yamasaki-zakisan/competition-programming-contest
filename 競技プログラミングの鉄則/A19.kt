fun main() {
    val (N, W) = readLine()!!.split(" ").map(String::toInt)
    // 2重配列の作成
    val dp = ArrayList(List(N+1) { ArrayList(List(W+1) { -1L }) })
    dp[0][0] = 0L
    for (h in 1..N) {
        val (w_p, v_p) = readLine()!!.split(" ").map(String::toInt)
        for (w in 0..W) {
            dp[h][w] = maxOf(dp[h-1][w], dp[h][w])
            if (dp[h-1][w] != -1L && w + w_p <= W) {
                dp[h][w+w_p] = maxOf(dp[h-1][w]+v_p, dp[h][w+w_p])
            }
        }
    }
    var ans = 0L
    for (d in dp) {
        ans = maxOf(d.max().toLong(), ans)
    }
    println(ans)
}
