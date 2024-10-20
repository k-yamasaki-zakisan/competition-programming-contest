// ２分探索
fun main() {
    val (N, K) = readLine()!!.split(" ").map(String::toInt)
    val A = readLine()!!.split(" ").map(String::toInt)
    var ans = 0L
    for (i in 0..N-1) {
        val target = K+A[i]
        var t_i = A.binarySearch(target+1)
        if (t_i < 0) {
            t_i = -t_i-2
        } else {
            t_i -= 1
        }
        if (i < t_i) {
            ans += t_i-i
        }
    }
    println(ans)
}