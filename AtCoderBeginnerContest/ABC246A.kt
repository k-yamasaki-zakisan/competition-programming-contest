fun main(){
    val xy = (1..3).map { readLine()!!.split(" ").map { it.toInt() } }
    if(xy[0][0] == xy[1][0]) {
        print(xy[2][0])
    } else if(xy[0][0] == xy[2][0]) {
        print(xy[1][0])
    } else {
        print(xy[0][0])
    }
    print(" ")
    if(xy[0][1] == xy[1][1]) {
        print(xy[2][1])
    } else if(xy[0][1] == xy[2][1]) {
        print(xy[1][1])
    } else { 
        println(xy[0][1])
    }
}