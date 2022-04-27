fun main() {
    val S = readLine()!!.toInt()
    val A = readLine()!!
    var x: Int = 0
    var y: Int = 0
    var dic = "EA"
    for (a in A) {
        if (a.toString() == "S") {
            if (dic == "NO") {
                y = y+1
            } else if (dic == "EA") {
                x = x+1
            } else if (dic == "SO") {
                y = y-1
            } else if (dic == "WE") {
                x = x-1
            }
        } else {
            if (dic == "NO") {
                dic = "EA"
            } else if (dic == "EA") {
                dic = "SO"
            } else if (dic == "SO") {
                dic = "WE"
            } else if (dic == "WE") {
                dic = "NO"
            }
        }
    }
    print(x)
    print(" ")
    print(y)
}