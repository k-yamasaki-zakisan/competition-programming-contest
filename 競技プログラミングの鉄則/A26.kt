fun main() {
    val Q = readLine()!!.trim().toInt()
    val Xs = List(Q) {
        readLine()!!.trim().toInt()
    }
    val maxVal = Xs.max()
    val memo = ArrayList(List(maxVal+1) { 0 })
    for (ori in 2 .. maxVal) {
        var next = ori
        while (next <= maxVal) {
            memo[next] += 1
            next += ori
        }
    }
    for (X in Xs) {
        println(if (memo[X] == 1) "Yes" else "No")
    }
}