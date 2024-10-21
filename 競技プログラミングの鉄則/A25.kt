fun main() {
    val (H, W) = readLine()!!.split(" ").map { it.toInt() }
    val C = List(H) {
        readLine()!!.trim()
    }
    val dp = ArrayList(List(H) { ArrayList(List(W) { 0L }) })
    dp[0][0] = 1
    for (h in 0 until H) {
        for (w in 0 until W) {
            if (C[h][w] == '#') continue
            if (h == 0 && w == 0) continue

            if (h == 0) {
                dp[h][w] = dp[h][w-1]
            } else if (w == 0) {
                dp[h][w] = dp[h - 1][w]
            } else {
                dp[h][w] = dp[h-1][w] +dp[h][w-1]
            }
        }
    }
    println(dp.last().last())
}