fun main() {
    val (N, K) = readLine()!!.split(" ").map(String::toInt)
    val A = readLine()!!.split(" ").map(String::toInt)
    val B = readLine()!!.split(" ").map(String::toInt)
    val C = readLine()!!.split(" ").map(String::toInt)
    val D = readLine()!!.split(" ").map(String::toInt)
    val memo = mutableMapOf<Int,Int>()
    for (c in C) {
        for (d in D) {
            val key = c+d
            memo[key] = memo.getOrDefault(key, 0) + 1
        }
    }
    for (a in A) {
        for (b in B) {
            val target = K-(a+b)
            if (memo.containsKey(target)) {
                println("Yes")
                return
            }
        }
    }
    println("No")
}