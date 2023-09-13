import Foundation

let K = Int(readLine()!)!
var arr: [Int] = []

for _ in 0..<K {
    let n = readLine()!
    if n == "0" {
        arr.removeLast()
    } else {
        arr.append(Int(n)!)
    }
}

var sum = 0
for i in arr {
    sum += i
}
print(sum)