fun main() {
    val (H, W) = readLine()!!.split(" ").map(String::toInt)
    val Xs = mutableListOf<List<Int>>()
    repeat(H) {
        val X = readLine()!!.split(" ").map(String::toInt)
        Xs.add(X)
    }
    val square = Array(H + 1) { IntArray(W + 1) }
    square[0][0] = Xs[0][0]

    for (h in 1..H-1) {
        square[h][0] = square[h-1][0] + Xs[h][0]
    }
    for (w in 1 .. W-1) {
        square[0][w] = square[0][w-1] + Xs[0][w]
    }
    for (h in 1..H-1) {
        for (w in 1 .. W-1) {
            square[h][w] = square[h-1][w] + square[h][w-1] - square[h-1][w-1] + Xs[h][w]
        }
    }
    val Q = readLine()!!.toInt()
    repeat(Q) {
        val (A, B, C, D) = readLine()!!.split(" ").map(String::toInt)
        var ans = square[C-1][D-1]
        if (1 < A) {
            ans -= square[A-2][D-1]
        }
        if (1 < B) {
            ans -= square[C-1][B-2]
        }
        if (1 < A && 1 < B) {
            ans += square[A-2][B-2]
        }
        println(ans)
    }
}