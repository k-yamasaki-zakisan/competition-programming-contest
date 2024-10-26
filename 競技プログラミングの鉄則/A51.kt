fun main() {
    val Q = readLine()!!.trim().toInt()
    val Querys = List(Q) {
        readLine()!!.split(" ").map { it.toString() }
    }
    val stackManage = mutableListOf<String>()
    for (i in 0 until Q) {
        if (Querys[i].first() == "1") {
            stackManage.add(Querys[i].last())
        }
        if (Querys[i].first() == "2") {
            println(stackManage.last())
        }
        if (Querys[i].first() == "3") {
            stackManage.removeAt(stackManage.size-1)
        }
    }
}