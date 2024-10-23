fun main() {
    val (N, X, Y) = readLine()!!.split(" ").map { it.toInt() }
    val A = readLine()!!.split(" ").map { it.toInt() }
    val maxNum = 100000 + 1
    val dp = ArrayList(List(maxNum) { 0 })
    for (i in 0 until maxNum) {
        val c = ArrayList(List(3) { true })
        if (X <= i) {
            c[dp[i - X]] = false
        }
        if (Y <= i) {
            c[dp[i - Y]] = false
        }
        for (j in 0 until 3) {
            if (c[j]) {
                dp[i] = j;
                break;
            }
        }
    }
    var ans = dp[A[0]]
    for (i in 1 until N) {
        ans = ans.xor(dp[A[i]])
    }
    println(if (ans == 0) "Second" else "First")
}