fun main() {
    val N = readLine()!!.trim().toInt()
    val A =  readLine()!!.split(" ").map { it.toInt() }
    val B =  readLine()!!.split(" ").map { it.toInt() }

    val sortA = A.sorted()
    val revSortB = B.sorted().reversed()
    var ans = 0
    for (i in 0 until N) {
        ans += sortA[i]*revSortB[i]
    }
    println(ans)
}