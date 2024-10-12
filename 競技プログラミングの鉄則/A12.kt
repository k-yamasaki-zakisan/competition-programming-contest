fun main() {
    val (N, K) = readLine()!!.split(" ").map(String::toInt)
    val A = readLine()!!.split(" ").map(String::toInt)
    var l = 0L
    var r = 10000000000L
    while (1 < r-l) {
        val mid = (r+l)/2
        var cnt = 0L
        for (a in A) {
            cnt += mid/a
        }
        if (K.toLong() <= cnt) {
            r = mid
        } else {
            l = mid
        }
    }
    println(r)
}