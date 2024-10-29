import java.util.PriorityQueue

fun main() {
    val (N, M) = readLine()!!.split(" ").map { it.toInt() }
    val ABCs = List(M) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    val root = mutableMapOf<Int, MutableList<Triple<Int, Int, Int>>>()
    for ((a, b, c, d) in ABCs) {
        root.computeIfAbsent(a-1) { mutableListOf() }.add(Triple(b-1, c, d))
        root.computeIfAbsent(b-1) { mutableListOf() }.add(Triple(a-1, c, d))
    }

    val visited = Array(N) { Int.MAX_VALUE }
    val stock = PriorityQueue<Pair<Int,Int>>(compareBy { it.first })
    stock.add(Pair(0,0))
    visited[0] = 0
    while (stock.isNotEmpty()) {
        val (now_w, now_i) = stock.poll()
        if (visited[now_i] < now_w) continue

        for ((next_i, w) in root.computeIfAbsent(now_i) { mutableListOf() }) {
            if (visited[now_i]+w < visited[next_i]) {
                visited[next_i] = visited[now_i]+w
                stock.add(Pair(visited[next_i],next_i))
            }
        }
    }

    val stockTree = PriorityQueue<Pair<Int,Int>>(compareByDescending { it.first })
    val trees = Array(N) { 0 }
    stockTree.add(Pair(0,N-1))
    while (stockTree.isNotEmpty()) {
        val (plus, now) = stockTree.poll()
        if (plus < trees[now]) continue
        for ((ex, c, d) in root.computeIfAbsent(now) { mutableListOf() }) {
            if (visited[now]-visited[ex] == c) {
                trees[ex] = maxOf(trees[now]+d, trees[ex])
                stockTree.add(Pair(trees[ex], ex))
            }
        }
    }
    println(visited.last().toString() + " " + trees.first().toString())
}