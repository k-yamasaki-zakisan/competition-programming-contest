fun main() {
    val S = readLine()!!.toInt()
    val A = readLine()!!.split(" ").map { it.toInt() }
    for (c in 0..2010) {
        if (c in A) continue
        print(c)
        break
    }
}