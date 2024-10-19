import java.util.PriorityQueue

fun main() {
    val N = readLine()!!.trim().toInt()
    val A = readLine()!!.trim().split(" ").filter { it.isNotEmpty() }.map { it.toInt() }
    val B = readLine()!!.trim().split(" ").filter { it.isNotEmpty() }.map { it.toInt() }
    val minHeap = PriorityQueue<Int>()
    minHeap.add(0)
    val memo = ArrayList(List(N) { 0 })
    val isVisited = ArrayList(List(N) { false })
    while (0 < minHeap.size) {
        val now = minHeap.poll()
        if (isVisited[now]) continue
        isVisited[now] = true
        val nextA = A[now]-1
        memo[nextA] = maxOf(memo[now] + 100, memo[nextA])
        if (nextA < N-1) {
            minHeap.add(nextA)
        }
        val nextB = B[now]-1
        memo[nextB] = maxOf(memo[now] + 150, memo[nextB])
        if (nextB < N-1) {
            minHeap.add(nextB)
        }
    }
    println(memo.last())
}
