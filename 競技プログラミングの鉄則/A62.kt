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

    val visited = Array(N) { false }
    val stock = mutableListOf<Int>()
    stock.add(0)
    visited[0] = true
    while (!stock.isEmpty()) {
        val now = stock.removeLast()

        for (next in root.computeIfAbsent(now) { mutableListOf() }) {
            if (visited[next]) continue
            visited[next] = true
            stock.add(next)
        }
    }

    println(if (visited.all { it }) "The graph is connected." else "The graph is not connected.")
}