import Foundation

let N = Int(readLine()!)!
var input = readLine()!.split(separator: " ").map { Int($0)! }
var stack: [Int] = []
var answer = Array(repeating: -1, count: N)

func NGE(i: Int) {
    while !stack.isEmpty && input[stack.last!] < input[i] {
        answer[stack.removeLast()] = input[i]
    }
    stack.append(i)
}

for i in 0..<N {
    NGE(i: i)
}

print(answer.map { String($0) }.joined(separator: " "))