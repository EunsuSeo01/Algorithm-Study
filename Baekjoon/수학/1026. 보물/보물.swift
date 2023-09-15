import Foundation

let N = Int(readLine()!)!
var A: [Int] = []
var B: [Int] = []

A += readLine()!.split(separator: " ").map { Int($0)! }
B += readLine()!.split(separator: " ").map { Int($0)! }

A.sort()
B.sort()

var sum = 0
for i in 0..<N {
    sum += A[i] * B[N-1-i]
}

print(sum)