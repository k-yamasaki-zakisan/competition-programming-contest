fun main() {
    val (n, m) = readLine()!!.split(" ").map { it.toInt() }
    val A = List(m) {
        readLine()!!.split(" ").map { it.toInt() }.take(n)
    }
    val inf = 1000
    val len_n = 1 shl n
    val dp = ArrayList(List(m+1) { ArrayList(List(len_n) { inf }) })
    dp[0][0] = 0
    for (i in 1..m) {
        for (bit in 0..len_n-1) {
            if (dp[i - 1][bit] == inf) {
                continue
            }
            dp[i][bit] = minOf(dp[i][bit], (dp[i - 1][bit]))
            var tmp = 0
            for (j in 0..n-1) {
                tmp += A[i-1][j] shl j
            }
            dp[i][bit or tmp] = minOf(dp[i][bit or tmp], (dp[i - 1][bit] + 1))
        }
    }
    println(if (dp[m][len_n - 1] == inf) -1 else dp[m][len_n - 1])
}
