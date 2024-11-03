class Solution {
    fun rotateString(s: String, goal: String): Boolean {
        if (s.length != goal.length) return false
        val n = s.length
        for (i in 0 until n) {
            var flag = true
            for (j in 0 until n) {
                if (goal[(i+j)%n] != s[j]) {
                    flag = false
                    break
                }
            }
            if (flag) return true
        }
        return false
    }
}