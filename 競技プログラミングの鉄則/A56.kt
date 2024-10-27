const val MOD = 1_000_000_007L
const val BASE = 31L

fun main() {
    val (N, Q) = readLine()!!.split(" ").map { it.toInt() }
    val S = readLine()!!.trim()
    val ABCDs = List(Q) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    val hash = LongArray(N + 1)
    val power = LongArray(N + 1)

    power[0] = 1
    for (i in 1..N) {
        power[i] = (power[i - 1] * BASE) % MOD
        hash[i] = (hash[i - 1] * BASE + (S[i - 1] - 'a' + 1)) % MOD
    }

    fun getHash(l: Int, r: Int): Long {
        return (hash[r] - hash[l - 1] * power[r - l + 1] % MOD + MOD) % MOD
    }

    for ((a,b,c,d) in ABCDs) {
        if (getHash(a, b) == getHash(c, d)) {
            println("Yes")
        } else {
            println("No")
        }
    }
}
