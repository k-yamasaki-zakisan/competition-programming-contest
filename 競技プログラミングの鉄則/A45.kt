fun main() {
    val (N, C) = readLine()!!.split(" ").map { it.toString() }
    val A = readLine()!!.trim()
    var cnt = 0
    for (a in A) {
        if (a.toString() == "R") {
            cnt += 1
        }
        if (a.toString() == "B") {
            cnt += 2
        }
        if (a.toString() == "W") {
            cnt += 0
        }
        cnt %= 3
    }

    if (C == "W" && cnt == 0 || C == "R" && cnt == 1 || C == "B" && cnt == 2) {
        println("Yes");
    } else {
        println("No")
    }
}