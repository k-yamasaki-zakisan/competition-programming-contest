fun main() {
    val N = readLine()!!.trim().toInt()
    var ans = 0L
    repeat(N) {
        val (T, A) = readLine()!!.split(" ")
        if (T == "+") {
            ans += A.toInt()
        }
        if (T == "-") {
            ans -= A.toInt()
        }
        if (T == "*") {
            ans *= A.toInt()
        }
        if (ans < 0) ans += 10000
        ans %= 10000
        println(ans)
    }
}