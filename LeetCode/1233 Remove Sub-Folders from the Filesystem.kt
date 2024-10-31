class Solution {
    fun removeSubfolders(folder: Array<String>): List<String> {
        val ans = mutableListOf<String>()
        folder.sort()
        for (f in folder) {
            var isUnique = true
            for (a in ans) {
                val cand = "$a/"
                if (f.startsWith(cand)) {
                    isUnique = false
                    break
                }
            }
            if (isUnique) {
                ans.add(f)
            }
        }
        return ans
    }
}