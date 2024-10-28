fun main() {
    val (N, Q) = readLine()!!.split(" ").map { it.toInt() }
    val Qs =  List(Q) {
        readLine()!!.split(" ").map { it.toInt() }
    }
    val sortQs = Qs.sortedBy { it[2] }
    val uf = UnionFind(N)
    var ans = 0
    for ((uF, uL, uCost) in sortQs) {
        if (uf.connected(uF-1, uL-1)) continue
        uf.union(uF-1, uL-1)
        ans += uCost
    }
    println(ans)
}

class UnionFind(size: Int) {
    private val parent = IntArray(size) { it }
    private val rank = IntArray(size) { 1 }

    fun find(x: Int): Int {
        if (parent[x] != x) {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    fun union(x: Int, y: Int) {
        val rootX = find(x)
        val rootY = find(y)

        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY
            } else {
                parent[rootY] = rootX
                rank[rootX] += 1
            }
        }
    }

    fun connected(x: Int, y: Int): Boolean {
        return find(x) == find(y)
    }
}