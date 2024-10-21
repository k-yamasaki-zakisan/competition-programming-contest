// 最大公約数
fun main() {
    val (A, B) = readLine()!!.split(" ").map { it.toLong() }
    println(gcd(A, B))
}

fun gcd(a: Long, b: Long): Long {
    return if (b == 0L) a else gcd(b, a % b)
}