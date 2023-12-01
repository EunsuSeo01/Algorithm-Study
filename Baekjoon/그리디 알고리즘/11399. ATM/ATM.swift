import Foundation

let N = Int(readLine()!)!
var input = readLine()!.split(separator: " ").map { Int($0)! }

input.sort()

var time = 0
var answer = 0
for i in input {
    answer += time + i
    time += i
}

print(answer)