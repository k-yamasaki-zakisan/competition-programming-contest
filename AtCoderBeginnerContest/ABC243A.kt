fun main() {
    val (V, A, B, C) = readLine()!!.split(" ").map { it.toInt() }
    val amari = V % (A + B + C)
    val ans = when {
        amari < A -> 'F'
        amari < A+B -> 'M'
        else -> 'T'
    }
    print(ans)
}