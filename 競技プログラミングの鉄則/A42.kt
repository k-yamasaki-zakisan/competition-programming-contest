fun main() {
    val (N, K) = readLine()!!.split(" ").map { it.toInt() }
    val AB = List(N) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    var ans = 0
    for (hp in 1..100) {
        for (magic in 1..100) {
            var cnt = 0
            for ((a, b) in AB) {
                if (hp <= a && a <= hp + K && magic <= b && b <= magic + K) {
                    cnt += 1
                }
            }
            ans = maxOf(ans, cnt)
        }
    }
    println(ans)
}