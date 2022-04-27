fun main() {
    val (A, B, C, D) = readLine()!!.split(" ").map { it.toInt() }
    if (A < C) {
        print("Takahashi")
	} else if(A == C && B <= D) {
        print("Takahashi")
	} else {
        print("Aoki")
	}
}