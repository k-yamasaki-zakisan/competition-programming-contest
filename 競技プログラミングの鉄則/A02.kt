fun main() {
  val (N, X) = readLine()!!.split(" ").map(String::toInt)
  val A = readLine()!!.split(" ").map(String::toInt)
  if (X in A) {
    println("Yes")
  } else {
    println("No")
  }
}