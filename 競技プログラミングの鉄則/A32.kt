fun main() {
    val (N, A, B) = readLine()!!.split(" ").map { it.toInt() }
    val dp = ArrayList(List(N + maxOf(A, B) + 1) { false })
    for (i in 0 .. N) {
        if (dp[i] == false) {
            dp[i + A] = true
            dp[i + B] = true
        }
    }
    println(if (dp[N]) "First" else "Second")
}