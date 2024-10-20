fun main() {
    val N = readLine()!!.trim().toInt()
    val A = readLine()!!.trim().split(" ").filter { it.isNotEmpty() }.map { it.toInt() }
    val lis = mutableListOf<Int>(A[0])
    for (a in A) {
        if (lis.last() < a) {
            lis.add(a)
        } else {
            var t_i = lis.binarySearch(a)
            if (t_i < 0) {
                t_i = -t_i-1
            }
            lis[t_i] = a
        }
    }
    println(lis.size)
}