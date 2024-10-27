fun main() {
    val (N, Q) = readLine()!!.split(" ").map { it.toInt() }
    val A = readLine()!!.split(" ").map { it.toInt() }
    val XYs = List(Q) {
        readLine()!!.split(" ").map { it.toLong() }
    }
    val dp = ArrayList(List(30) { ArrayList(List(N) { 0 }) })
    for (i in 0 until N) {
        dp[0][i] = A[i]-1
    }
    for (i in 1 until 30) {
        for (j in 0 until N) {
            dp[i][j] = dp[i - 1][dp[i - 1][j]]
        }
    }
    for ((x, y) in XYs) {
        var pos = (x - 1).toInt()
        for (i in 29 downTo 0) {
            if (y and (1L shl i) != 0L) {
                pos = dp[i][pos]
            }
        }
        println(pos + 1)
    }
}