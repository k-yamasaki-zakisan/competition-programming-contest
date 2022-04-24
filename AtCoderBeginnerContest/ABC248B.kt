fun main(args: Array<String>) {
    val (a, b, k) = readLine()!!.split(" ").map { it.toInt() }

    var cur = a.toLong()
    var ans = 0
    while (cur < b) {
        cur *= k
        ans++
    }
    println(ans)
}