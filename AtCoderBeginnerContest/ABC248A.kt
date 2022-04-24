fun main() {
	val S = readLine()!!
	for (c in '0' .. '9') {
		if (!S.contains(c))
			println(c)
	}
}