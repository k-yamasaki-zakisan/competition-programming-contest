fun main() {
    val (N, M) = readLine()!!.split(" ").map { it.toInt() }
    val ABs = List(M) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    val root = mutableMapOf<Int, MutableList<Int>>()
    for ((a, b) in ABs) {
        root.computeIfAbsent(a-1) { mutableListOf() }.add(b-1)
        root.computeIfAbsent(b-1) { mutableListOf() }.add(a-1)
    }

    val visited = Array(N) { -1 }
    val stock = ArrayDeque<Int>()
    stock.add(0)
    visited[0] = 0
    while (!stock.isEmpty()) {
        val now = stock.removeFirst()

        for (next in root.computeIfAbsent(now) { mutableListOf() }) {
            if (visited[next] != -1) continue
            visited[next] = visited[now]+1
            stock.add(next)
        }
    }

    for (diff in visited) {
        println(diff)
    }
}