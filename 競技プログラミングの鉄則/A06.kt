fun main() {
    val (N, K) = readLine()!!.split(" ").map(String::toInt)
    val A = readLine()!!.split(" ").map(String::toInt)
    val cnt = MutableList(N) { 0 }
    cnt[0] = A[0]
    for (i in (1..N-1)) {
        cnt[i] = cnt[i-1] + A[i]
    }
    println(cnt)
    for (i in (0..K-1)) {
        val (l, r) = readLine()!!.split(" ").map(String::toInt)
        var ans = cnt[r-1]
        if (1 < l) {
            ans -= cnt[l-2]
        }
        println(ans)
    }
}