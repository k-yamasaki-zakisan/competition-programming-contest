fun main() {
    val N = readLine()!!.trim().toInt()
    val S = readLine()!!.toString().toCharArray().map { it.toString() }
    for (i in 1 until N-1) {
        if (S[i-1] == S[i] && S[i] == S[i+1]) {
            println("Yes")
            return
        }
    }
    println("No")
}