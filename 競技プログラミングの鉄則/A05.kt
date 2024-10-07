fun main() {
    val (N, K) = readLine()!!.split(" ").map(String::toInt)
    var ans: Int = 0
    for (i in 1..N) {
        for (j in 1..N) {
            var tmp: Int = K-(i+j)
            if (tmp in 1..N) {
                ans += 1
            }
        }
    }
    println(ans)
}