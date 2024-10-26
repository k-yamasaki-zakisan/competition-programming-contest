fun main() {
    val Q = readLine()!!.trim().toInt()
    val Querys = List(Q) {
        readLine()!!.split(" ").map { it.toString() }
    }
    val queue: ArrayDeque<String> = ArrayDeque()
    for (i in 0 until Q) {
        if (Querys[i].first() == "1") {
            queue.add(Querys[i].last())
        }
        if (Querys[i].first() == "2") {
            println(queue.first())
        }
        if (Querys[i].first() == "3") {
            queue.removeFirst()
        }
    }
}