fun main() {
    val D = readLine()!!.toInt()
    val N = readLine()!!.toInt()
    val cnt = MutableList(D) { 0 }
    for (i in (0..N-1)) {
        val (L, R) = readLine()!!.split(" ").map(String::toInt)
        if (R < D) {
            cnt[R] -= 1
        }
        cnt[L-1] += 1
    }
    for (i in (1..D-1)) {
        cnt[i] = cnt[i-1] + cnt[i]
    }
    for (i in (0..D-1)) {
        println(cnt[i])
    }
}