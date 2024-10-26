fun main() {
    val N = readLine()!!.trim().toInt()
    val XYs = List(N) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    for (i in 0 until N) {
        println("AB"[i%2])
    }
}