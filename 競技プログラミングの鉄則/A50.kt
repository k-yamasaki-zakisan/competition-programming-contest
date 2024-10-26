import kotlin.random.Random

fun main() {
    val N = 100
    val A = List(N) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    val X = ArrayList(List(1000) { 0 })
    val Y = ArrayList(List(1000) { 0 })
    val H = ArrayList(List(1000) { 0 })
    for (i in 0 until 1000) {
        val x = Random.nextInt(0, N)
        val y = Random.nextInt(0, N)
        X[i] = x
        Y[i] = y
        H[i] = 1
    }
    println(1000)
    for (i in 0 until 1000) {
        println(X[i].toString() + ' ' + Y[i].toString() + ' ' + H[i].toString())
    }
}