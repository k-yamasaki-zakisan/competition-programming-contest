fun main() {
    val (N, M, B) = readLine()!!.split(" ").map { it.toLong() }
    val A = readLine()!!.split(" ").map { it.toLong() }
    val C = readLine()!!.split(" ").map { it.toLong() }
    val cSum = C.sum()
    var ans = 0L
    for (a in A) {
        ans += (a*M)+cSum+B*M
    }
    println(ans)
}