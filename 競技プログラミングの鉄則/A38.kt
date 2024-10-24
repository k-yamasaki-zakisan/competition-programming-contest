// heap系の問題
import java.util.PriorityQueue

fun main() {
    val (D, N) = readLine()!!.split(" ").map { it.toInt() }
    val LRH = List(N) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    val sortedLRH = LRH.sortedBy { it[0] }

    // 2次元配列を最初の要素の小さい順に管理するヒープを作成
    val pq = PriorityQueue<Array<Int>>(compareBy { it[0] })
    var nowLrhI = 0
    var ans = 0
    for (i in 1..D) {
        while (nowLrhI < N && sortedLRH[nowLrhI][0] == i) {
            pq.add(arrayOf(sortedLRH[nowLrhI][2], sortedLRH[nowLrhI][1]))
            nowLrhI += 1
        }
        while (!pq.isEmpty() && pq.peek()[1] < i) {
            pq.poll()
        }
        ans += if (pq.isEmpty()) 24 else pq.peek()[0]
    }
    println(ans)
}
