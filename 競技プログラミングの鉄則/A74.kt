fun main() {
    val N = readLine()!!.trim().toInt()
    val Ps = List(N) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    val points = mutableMapOf<Int, Pair<Int, Int>>()
    for (h in 0 until N) {
        for (w in 0 until N) {
            if (0 < Ps[h][w]) {
                points[Ps[h][w]] = Pair(h+1, w+1)
            }
        }
    }
    var ans = 0
    for (num in 1 .. N) {
        val h = points[num]?.first ?: 0
        val w = points[num]?.second ?: 0
        ans += maxOf(h-num, 0)
        ans += maxOf(w-num, 0)
        for (numSecond in num .. N) {
            var newH = points[numSecond]?.first ?: 0
            if (newH < h) newH += 1
            var newW = points[numSecond]?.second ?: 0
            if (newW < w) newW += 1
            points[numSecond] = Pair(newH, newW)
        }
    }
    println(ans)
}