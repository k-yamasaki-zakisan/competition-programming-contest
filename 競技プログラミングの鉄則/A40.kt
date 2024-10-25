// nCiの高速化
fun main() {
    val N = readLine()!!.trim().toInt()
    val A = readLine()!!.split(" ").map { it.toInt() }
    val frequencyMap = A.groupingBy { it }.eachCount()
    val mod = 1000000007L
    var ans = 0L
    val fact = ArrayList(List(N+1) { 1L })
    val factInv = ArrayList(List(N+1) { 1L })
    for (i in 1..N) {
        fact[i] = (fact[i-1] * i) % mod
    }
    factInv[N] = modPow(fact[N],mod-2, mod)
    for (i in N downTo 1) {
        factInv[i-1] = (i * factInv[i]) % mod
    }
    for ((key, cnt) in frequencyMap) {
        if (3 <= cnt) {
            ans += comb(cnt, 3, mod, fact, factInv)
        }
    }
    println(ans)
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