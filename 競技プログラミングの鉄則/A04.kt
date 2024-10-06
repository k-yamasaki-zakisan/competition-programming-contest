fun main() {
  val N = readLine()!!.toInt()
  val binary: String = Integer.toBinaryString(N).padStart(10, '0')
  println(binary)
}