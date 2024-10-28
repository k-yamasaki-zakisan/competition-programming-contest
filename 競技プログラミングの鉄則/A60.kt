fun main() {
    val N = readLine()!!.trim().toInt()
    val A = readLine()!!.split(" ").map { it.toInt() }

    val ans = ArrayList(List(N) { -1 })
    val stock = mutableListOf<Pair<Int, Int>>()
    for (i in 0 until N) {
        while (!stock.isEmpty()) {
            val (k, v) = stock.last()
            if (A[i] < v) {
                ans[i] = k + 1
                break;
            } else {
                stock.removeLast();
            }
        }
        stock.add(Pair(i, A[i]))
    }
    println(ans.joinToString(" "))
}