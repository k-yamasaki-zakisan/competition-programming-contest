fun main() {
    val (H, W, N) = readLine()!!.split(" ").map(String::toInt)
    val ABCD = mutableListOf<List<Int>>()
    repeat(N) {
        val x = readLine()!!.split(" ").map(String::toInt)
        ABCD.add(x)
    }
    val square = Array(H) { IntArray(W) }
    for ((a,b,c,d) in ABCD) {
        square[a-1][b-1] += 1
        if (c < H && d < W) {
            square[c][d] += 1
        }
        if (c < H) {
            square[c][b-1] -= 1
        }
        if (d < W) {
            square[a-1][d] -= 1
        }
    }
    for (h in 0..H-1) {
        for (w in 1 .. W-1) {
            square[h][w] += square[h][w-1]
        }
    }
    for (w in 0..W-1) {
        for (h in 1 .. H-1) {
            square[h][w] += square[h-1][w]
        }
    }
    
    for (sq in square) {
        val s_str = sq.joinToString(" ")
        println(s_str)
    }
}