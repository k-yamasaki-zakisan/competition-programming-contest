fun main() {
    val (N, S) = readLine()!!.split(" ").map(String::toInt)
    val A = readLine()!!.trim().split(" ").filter { it.isNotEmpty() }.map { it.toInt() }
    val splitIndex = (N + 1) / 2
    val firstHalf = A.subList(0, splitIndex)
    val secondHalf = A.subList(splitIndex, N)
    val dpFirst = IntArray(S+1) { 0 }
    dpFirst[0] = 1
    for (a in firstHalf) {
        for (i in S downTo  0) {
            if (dpFirst[i] == 1 && i+a <= S) {
                dpFirst[i+a] = 1
            }
        }
    }
    val dpSecond = IntArray(S+1) { 0 }
    dpSecond[0] = 1
    for (a in secondHalf) {
        for (i in  S downTo  0) {
            if (dpSecond[i] == 1 && i+a <= S) {
                dpSecond[i+a] = 1
            }
        }
    }
    for (i in 0..S) {
        if (dpFirst[i] == 1 && dpSecond[S-i] == 1) {
            println("Yes")
            return
        }
    }
    println("No")
}
