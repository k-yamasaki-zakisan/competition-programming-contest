class Solution {
    fun shortestDistanceAfterQueries(n: Int, queries: Array<IntArray>): IntArray {
        val root: MutableList<MutableList<Int>> = MutableList(n) { mutableListOf() }
        for (i in 1 until n) {
            root[i-1].add(i)
        }
        val ans = IntArray(queries.size) { -1 }
        for (i in 0 until queries.size) {
            val (f, l) = queries[i]
            root[f].add(l)
            val step = MutableList(n) { -1 }
            step[0] = 0
            val queue = ArrayDeque(mutableListOf(0))
            while (!queue.isEmpty()) {
                val now = queue.removeFirst()
                for (next in root[now]) {
                    if (step[next] != -1) continue
                    step[next] = step[now] + 1
                    queue.add(next)
                }
            }
            ans[i] = step.last()
        }
        return ans
    }
}