fun main() {
    val N = readLine()!!.trim().toInt()
    val A = readLine()!!.split(" ").map { it.toInt() }
    val rootDown = mutableMapOf<Int, MutableList<Int>>()
    val rootUp = mutableMapOf<Int, Int>()
    for (i in 0 until N-1) {
        rootDown.computeIfAbsent(A[i]-1) { mutableListOf() }.add(i+1)
        rootUp[i+1] = A[i]-1
    }

    val deepCount = Array(N) { -1 }
    val stock = ArrayDeque<Int>()
    stock.add(0)
    deepCount[0] = 0
    while (stock.isNotEmpty()) {
        val now = stock.removeFirst()

        for (next in rootDown.computeIfAbsent(now) { mutableListOf() }) {
            if (deepCount[next] != -1) continue
            deepCount[next] = deepCount[now]+1
            stock.add(next)
        }
    }

    val maxCnt = deepCount.max()
    val ans = Array(N) { 0 }
    val cntMap = mutableMapOf<Int, MutableList<Int>>()
    for (i in 0 until N) {
        cntMap.computeIfAbsent(deepCount[i]) { mutableListOf() }.add(i)
    }
    for (i in maxCnt downTo  1) {
        for (now in cntMap.computeIfAbsent(i) { mutableListOf() }) {
            ans[rootUp[now]!!] += ans[now] + 1
        }
    }
    println(ans.joinToString(" "))
}