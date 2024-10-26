import java.util.PriorityQueue

fun main() {
    val Q = readLine()!!.trim().toInt()
    val Querys = List(Q) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    val priorityQueue: PriorityQueue<Int> = PriorityQueue()
    for (i in 0 until Q) {
        if (Querys[i].first() == 1) {
            priorityQueue.add(Querys[i].last())
        }
        if (Querys[i].first() == 2) {
            println(priorityQueue.peek())
        }
        if (Querys[i].first() == 3) {
            priorityQueue.poll()
        }
    }
}