import kotlin.math.sqrt

fun main() {
    val (a, b) = readLine()!!.split(" ").map { it.toDouble() }
    val ab = sqrt(a*a + b*b)
    println("${a/ab} ${b/ab}")
}