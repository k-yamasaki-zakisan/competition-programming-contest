fun main() {
    val N = readLine()!!.trim().toInt()
    val A = readLine()!!.split(" ").map { it.toLong() }
    val dp = ArrayList(List(N) { ArrayList(List(N) { 0L }) })
    dp[N - 1] = ArrayList(A)
    for (i in N-2 downTo 0) {
        for (j in 0 until i+1) {
            if (i%2 == 0) {
                dp[i][j] = maxOf(dp[i + 1][j], dp[i + 1][j + 1])
            } else {
                dp[i][j] = minOf(dp[i + 1][j], dp[i + 1][j + 1])
            }
        }
    }
    println(dp[0][0])
}