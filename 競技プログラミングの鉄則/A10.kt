fun main() {
    val N = readLine()!!.toInt()
    val A = readLine()!!.split(" ").map(String::toInt)
    val l_scan = Array(N) {0}
    l_scan[0] = A.first()
    for (i in 1..N-1) {
        l_scan[i] = maxOf(l_scan[i-1], A[i])
    }
    val r_scan = Array(N) {0}
    r_scan[N-1] = A.last()
    for (i in N-2 downTo 0) {
        r_scan[i] = maxOf(r_scan[i+1], A[i])
    }
    val Q = readLine()!!.toInt()
    repeat(Q) {
        val (L, R) = readLine()!!.split(" ").map(String::toInt)
        val ans = maxOf(l_scan[L - 2], r_scan[R])
        println(ans)
    }
}