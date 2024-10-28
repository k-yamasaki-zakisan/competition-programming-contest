class SegmentTree(private val size: Int) {
    private val tree = LongArray(2 * size) { 0L }

    // 値の更新：A[pos] を x に変更
    fun update(pos: Int, value: Long) {
        var p = pos + size
        tree[p] = value
        while (p > 1) {
            p /= 2
            tree[p] = maxOf(tree[2 * p], tree[2 * p + 1])
        }
    }

    // 範囲最大値クエリ：A[l] から A[r-1] の最大値を返す
    fun rangeMax(l: Int, r: Int): Long {
        var left = l + size
        var right = r + size
        var maxVal = Long.MIN_VALUE

        while (left < right) {
            if (left % 2 == 1) {
                maxVal = maxOf(maxVal, tree[left])
                left++
            }
            if (right % 2 == 1) {
                right--
                maxVal = maxOf(maxVal, tree[right])
            }
            left /= 2
            right /= 2
        }
        return maxVal
    }
}

fun main() {
    val (N, Q) = readLine()!!.split(" ").map { it.toInt() }

    val segmentTree = SegmentTree(N)

    repeat(Q) {
        val (type, pos, x) = readLine()!!.split(" ").map { it.toInt() }
        if (type == 1) {
            segmentTree.update(pos-1, x.toLong())
        } else if (type == 2) {
          println(segmentTree.rangeMax(pos-1, x-1))
        }
    }

}