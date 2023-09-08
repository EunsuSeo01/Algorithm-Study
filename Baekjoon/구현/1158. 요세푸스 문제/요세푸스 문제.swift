import Foundation

var input = readLine()!.split(separator: " ")
let N = Int(input[0])!
let K = Int(input[1])!
var arr: [Int] = []
for i in 1...N {
    arr.append(i)
}

var index = 0
var result: [Int] = []
while arr.count > 0 {
    index = (K-1) % arr.count
    result.append(arr[index])
    arr.remove(at: index)
    if index != 0 {
        arr.append(contentsOf: arr[0..<index])
        arr.removeSubrange(0..<index)
    }
}

print("<", terminator: "")
for i in result {
    if i == result.last {
        print("\(i)", terminator: "")
    } else {
        print("\(i), ", terminator: "")
    }
}
print(">")