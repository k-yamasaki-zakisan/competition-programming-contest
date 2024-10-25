fun main() {
    val (N, L) = readLine()!!.split(" ").map { it.toInt() }
    val AB = List(N) {
        readLine()!!.split(" ")
    }
    var ans = 0
    for ((a, b) in AB) {
        ans = maxOf(ans, if (b == "E") L-a.toInt() else a.toInt())
    }
    println(ans)
}