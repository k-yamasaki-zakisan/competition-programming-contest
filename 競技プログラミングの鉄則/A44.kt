fun main() {
    val (N, Q) = readLine()!!.split(" ").map { it.toInt() }
    val Queries = List(Q) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    val a = ArrayList(List(N) { it + 1 })
    var isRevers = false
    for (q in Queries) {
        if (q.first() == 1) {
            if (!isRevers) {
                a[q[1]-1] = q.last()
            } else {
                a[N-q[1]] = q.last()
            }
        } else if (q.first() == 2) {
            isRevers = !isRevers
        } else {
            if (!isRevers) {
                println(a[q.last()-1])
            } else {
                println(a[N-q.last()])
            }
        }
    }
}