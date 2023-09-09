import Foundation

let A = Int(readLine()!)!
let T = Int(readLine()!)!
let signal = Int(readLine()!)!

var members: [Int] = []
for _ in 0..<A {
    members.append(0)
}

var times = 2
var index = 0
var count = 0
var num = 1

while true {
    var arr = [0,1,0,1]
    for _ in 0..<times {
        arr.append(0)
    }
    for _ in 0..<times {
        arr.append(1)
    }
    
    for n in arr {
        if n == signal {
            count += 1
        }
        if count == T {
            print(index)
            exit(0)
        }
        index += 1
        index %= A
    }
    times += 1
}