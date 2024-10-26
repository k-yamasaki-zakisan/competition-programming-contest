import java.util.TreeSet

fun main() {
    val Q = readLine()!!.trim().toInt()
    val Querys = List(Q) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    val treeSet = TreeSet<Int>()
    for (i in 0 until Q) {
        if (Querys[i].first() == 1) {
            treeSet.add(Querys[i].last())
        }
        if (Querys[i].first() == 2) {
            treeSet.remove(Querys[i].last())
        }
        if (Querys[i].first() == 3) {
            println(treeSet.ceiling(Querys[i].last())?: -1)
        }
    }
}