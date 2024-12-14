import java.util.PriorityQueue
import kotlin.math.sqrt

class Solution {
    fun pickGifts(gifts: IntArray, k: Int): Long {
        val maxHeap = PriorityQueue<Long>(compareByDescending { it }).apply {
            addAll(gifts.map { it.toLong() })
        }
        for(i in 0 until k) {
            val num = maxHeap.poll()
            maxHeap.add(sqrt(num.toDouble()).toLong())
        }
        // println(maxHeap)
        return maxHeap.sum()
    }
}