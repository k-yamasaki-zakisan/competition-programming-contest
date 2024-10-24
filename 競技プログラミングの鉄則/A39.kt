fun main() {
    val N = readLine()!!.trim().toInt()
    val LR = List(N) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    val sortedLR = LR.sortedWith(compareBy({ it[1] }, { -it[0] }))

    var ans = 0
    var nowDay = -1
    for ((l, r) in sortedLR) {
        if (nowDay <= l) {
            nowDay = r
            ans += 1
        }
    }
    println(ans)
}