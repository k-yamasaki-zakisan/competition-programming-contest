fun main() {
    val (H, W, K) = readLine()!!.split(" ").map { it.toInt() }
    val Cs = List(H) {
        readLine()!!.trim().toCharArray()
    }
    var ans = 0

    for (i in 0 until (1 shl H)) {
        val hChoices = mutableListOf<Int>()
        for (j in 0 until H) {
            if ((1 shl j) and i == 0) {
                hChoices.add(j)
            }
        }
        if (K < hChoices.size) continue
        var cnt = hChoices.size * W
        val wCnts = mutableListOf<Int>()

        for (w_i in 0 until W) {
            var tmp = 0
            for (h_i in 0 until H) {
                if (h_i in hChoices) continue
                if (Cs[h_i][w_i] == '#') {
                    tmp += 1
                }
            }
            wCnts.add(tmp)
        }
        wCnts.sort()
        for (i in 0 until (K - hChoices.size)) {
            cnt += H - hChoices.size
        }
        for (i in (K - hChoices.size) until W) {
            cnt += wCnts[i]
        }
        ans = maxOf(ans, cnt)
    }
    println(ans)
}