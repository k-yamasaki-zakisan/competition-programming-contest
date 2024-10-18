fun main() {
    val N = readLine()!!.trim().toInt()
    val pValues = mutableListOf<Int>(0)
    val aValues = mutableListOf<Int>(0)
    repeat(N) {
        val (P, A) = readLine()!!.split(" ").map(String::toInt)
        pValues.add(P)
        aValues.add(A)
    }
    val dp = ArrayList(List(N+2) { ArrayList(List(N+2) { 0 }) })
    for (len in N - 1 downTo 1) {
        for (l in 1 .. N - len + 1) {
            val r = l + len - 1
            if (l == 1) dp[l][r] = dp[l][r + 1] + if (pValues[r + 1] in l .. r) aValues[r + 1] else 0
            else if (r == N) dp[l][r] = dp[l - 1][r] + if (pValues[l - 1] in l .. r) aValues[l - 1] else 0
            else dp[l][r] = maxOf(dp[l][r + 1] + if (pValues[r + 1] in l .. r) aValues[r + 1] else 0, dp[l - 1][r] + if (pValues[l - 1] in l .. r) aValues[l - 1] else 0)
        }
    }
    var ans = 0
    for ( i in 0..N) {
        ans = maxOf(ans, dp[i][i])
    }
    println(ans)
}
