fun main() {
    val (N, M) = readLine()!!.split(" ").map { it.toInt() }
    val ABs = List(M) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    val ans = mutableMapOf<Int, MutableList<Int>>()
    for ((a, b) in ABs) {
        // mapのvaluesを配列で設定する場合の初期化式
        ans.computeIfAbsent(a) { mutableListOf() }.add(b)
        ans.computeIfAbsent(b) { mutableListOf() }.add(a)
    }

    for (i in 1..N) {
        println("$i: {${ans.computeIfAbsent(i) { mutableListOf() }.joinToString(", ")}}")
    }
}