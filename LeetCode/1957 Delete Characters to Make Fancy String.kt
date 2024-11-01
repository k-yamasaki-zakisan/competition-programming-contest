class Solution {
    fun makeFancyString(s: String): String {
        var ans  = StringBuilder()
        var cnt = 0
        var exS = "-1"
        for (sChar in s) {
            val sString = sChar.toString()
            if (exS == sString) {
                cnt += 1
            } else {
                exS = sString
                cnt = 1
            }

            if (cnt < 3) {
                ans.append(sChar.toString())
            }
        }
        return ans.toString()
    }
}