// nCrの高速計算
fun main() {
    val (n, r) = readLine()!!.split(" ").map { it.toInt() }
    val mod = 1000000007L
    val fact = ArrayList(List(n+1) { 1L })
    val factInv = ArrayList(List(n+1) { 1L })
    for (i in 1..n) {
        fact[i] = (fact[i-1] * i) % mod
    }
    factInv[n] = modPow(fact[n],mod-2, mod)
    for (i in n downTo 1) {
        factInv[i-1] = (i * factInv[i]) % mod
    }
    println(comb(n,r,mod, fact, factInv))
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

fun comb(n: Int, r: Int, mod: Long, fact: ArrayList<Long>, factInv: ArrayList<Long>): Long {
    return (fact[n] % mod * factInv[r] % mod * factInv[n-r]) % mod
}