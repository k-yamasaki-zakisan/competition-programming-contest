fun main() {
    val (N, M) = readLine()!!.split(" ").map { it.toInt() }
    val ABCs =  List(M) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    val edges = ArrayList(List(N + 1) { mutableListOf<MutableList<Int>>() })
    for ((a, b, c) in ABCs) {
        edges[a].add(mutableListOf(b, c, edges[b].size))
        edges[b].add(mutableListOf(a, 0, edges[a].size - 1))
    }

    fun getFlowDfs(pos: Int, goal: Int, F: Int, visited: ArrayList<Boolean>): Int {
        if (pos == goal) return F
        visited[pos] = true

        for (i in 0 until edges[pos].size) {
            val (to, cap, rev) = edges[pos][i]
            if (visited[to]) continue
            if (cap == 0) continue

            val flow = getFlowDfs(to, goal, minOf(F, cap), visited)
            if (0 < flow) {
                edges[to][rev][1] += flow
                edges[pos][i][1] -= flow
                return flow
            }
        }
        return 0
    }

    var ans = 0
    while (true) {
        val visited = ArrayList(List(N + 1) { false })
        val flow = getFlowDfs(1, N, 5000, visited)
        if (flow == 0) break
        ans += flow
    }
    println(ans)
}