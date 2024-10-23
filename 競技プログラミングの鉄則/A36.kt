fun main() {
    val (N, K) = readLine()!!.split(" ").map { it.toLong() }
    val totalCnt = (N-1)*2
    if (K < totalCnt) {
        println("No")
    } else if ((K-totalCnt)%2 == 0L) {
        println("Yes")
    } else {
        println("No")
    }
}