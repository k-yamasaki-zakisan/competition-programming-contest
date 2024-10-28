import java.util.PriorityQueue

fun main() {
    val (N, M) = readLine()!!.split(" ").map { it.toInt() }
    val ABCs = List(M) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    val root = mutableMapOf<Int, MutableList<Pair<Int, Int>>>()
    for ((a, b, c) in ABCs) {
        root.computeIfAbsent(a-1) { mutableListOf() }.add(Pair(b-1, c))
        root.computeIfAbsent(b-1) { mutableListOf() }.add(Pair(a-1, c))
    }

    val visited = Array(N) { Long.MAX_VALUE }
    val stock = PriorityQueue<Pair<Long,Int>>(compareBy { it.first })
    stock.add(Pair(0L,0))
    visited[0] = 0L
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

    for (diff in visited) {
        println(if (diff == Long.MAX_VALUE) -1 else diff)
    }
}