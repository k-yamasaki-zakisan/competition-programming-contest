fun main() {
    val S = readLine()!!.trim().toString()
    val T = readLine()!!.trim().toString()
    val s_size = S.length
    val t_size = T.length
    val dp = ArrayList(List(s_size+1) { ArrayList(List(t_size+1) { 0 }) })
    for (i in 1..s_size) {
        for (j in 1..t_size) {
            if (S[i-1] == T[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1
            } else {
                dp[i][j] = maxOf(dp[i][j-1], dp[i-1][j])
            }
        }
    }
    println(dp[s_size][t_size])
}