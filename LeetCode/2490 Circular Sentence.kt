class Solution {
    fun isCircularSentence(sentence: String): Boolean {
        val words = sentence.split(" ")
        var flag = sentence.first() == sentence.last()
        for (i in 1 until words.size) {
            if (words[i-1].last() != words[i].first()) {
                flag = false
            }
            if (!flag) return flag
        }
        return flag
    }
}