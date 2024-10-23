fun main() {
    val N = readLine()!!.trim().toLong()
    val A = readLine()!!.split(" ").map { it.toLong() }
    var ans = 0L
    for (a in A) {
        ans = ans.xor(a)
    }
    println(if (ans == 0L) "Second" else "First")
}