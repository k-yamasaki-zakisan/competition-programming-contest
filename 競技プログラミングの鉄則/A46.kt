fun main() {
    val N = readLine()!!.trim().toInt()
    val XYs = List(N) {
        readLine()!!.split(" ").map { it.toLong() }
    }
    println(1)
    var now = 0
    var visited = ArrayList(List(N) { false })
    visited[0] = true
    repeat(N - 1) {
        val (nowx, nowy) = XYs[now];
        var tmp = 10000000000
        var tmp_position = now
        for (i in 0 until N) {
            if (visited[i]) continue
            val (nextx, nexty) = XYs[i]
            var diff = 0L
            if (nextx != nowx) {
                if (nextx < nowx) {
                    diff += modPow((nowx - nextx), 2);
                } else {
                    diff += modPow((nextx - nowx), 2);
                }
            }
            if (nexty != nowy) {
                if (nexty < nowy) {
                    diff += modPow((nowy - nexty), 2);
                } else {
                    diff += modPow((nexty - nowy), 2);
                }
            }
            if (diff < tmp) {
                tmp = diff
                tmp_position = i
            }
        }
        now = tmp_position
        visited[now] = true
        println(now + 1)
    }
    println(1)
}

fun modPow(a: Long, b: Long): Long {
    var result = 1L
    var base = a
    var exponent = b

    while (exponent > 0) {
        if (exponent % 2 == 1L) {
            result = (result * base)
        }
        base = (base * base)
        exponent /= 2
    }
    return result
}