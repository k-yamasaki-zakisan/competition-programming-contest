// 繰り返し２乗法 pow
fun main() {
    val (A, B) = readLine()!!.split(" ").map { it.toLong() }
    val mod = 1000000007L
    println(modPow(A, B, mod))
}

fun modPow(a: Long, b: Long, mod: Long): Long {
    var result = 1L
    var base = a % mod
    var exponent = b

    while (exponent > 0) {
        if (exponent % 2 == 1L) {
            result = (result * base) % mod
        }
        base = (base * base) % mod
        exponent /= 2
    }
    return result
}