fun main() {
    val N = readLine()!!.trim().toInt()
    val A = readLine()!!.trim().split(" ").filter { it.isNotEmpty() }.map { it.toInt() }
    val a_sort = A.toSet().toList().sorted()
    val a_map = mutableMapOf<Int, Int>()
    for (i in 0 .. a_sort.size-1) {
        a_map[a_sort[i]] = i+1
    }
    val ans = mutableListOf<Int>()
    for (i in 0..N-1) {
        ans.add(a_map.getValue(A[i]))
    }
    println(ans.joinToString(" "))
}