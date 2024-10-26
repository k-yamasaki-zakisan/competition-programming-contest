fun main() {
    val Q = readLine()!!.trim().toInt()
    val Querys = List(Q) {
        readLine()!!.split(" ").map { it.toString() }
    }
    val mapMemok= mutableMapOf<String, String>()
    for (i in 0 until Q) {
        if (Querys[i].first() == "1") {
            mapMemok[Querys[i][1]] = Querys[i].last()
        }
        if (Querys[i].first() == "2") {
            println(mapMemok[Querys[i][1]])
        }
    }
}