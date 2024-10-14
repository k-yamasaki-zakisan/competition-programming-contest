fun main() {
    val N = readLine()!!.trim().toInt()
    val A = readLine()!!.trim().split(" ").filter { it.isNotEmpty() }.map { it.toInt() }
    val B = readLine()!!.trim().split(" ").filter { it.isNotEmpty() }.map { it.toInt() }
    val dp = IntArray(N) { 0 }
    dp[1] = A[0]
    for (i in 2..N-1) {
        dp[i] = minOf(dp[i-1]+A[i-1], dp[i-2]+B[i-2])
    }
    val ans = mutableListOf<Int>(N)
    var i = N-1
    while (0 < i) {
        if (dp[i]-dp[i-1] == A[i-1]) {
            ans.add(i)
            i -= 1
        } else {
            ans.add(i-1)
            i -= 2
        }
    }
    println(ans.size)
    println(ans.asReversed().joinToString(" "))
}
