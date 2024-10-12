fun main() {
    val (N, X) = readLine()!!.split(" ").map(String::toInt)
    val A = readLine()!!.split(" ").map(String::toInt)
    val i = A.binarySearch(X)+1
    println(i)
}