import Foundation

let N = Int(readLine()!)!
var input: [Int] = []
var result = 0

for _ in 0..<N {
    input.append(Int(readLine()!)!)
}

input.sort()

while !input.isEmpty {
    if input.count > 2 {
        result += input.popLast() ?? 0
        result += input.popLast() ?? 0
        input.popLast()
    } else {
        for i in input {
            result += input.popLast() ?? 0
        }
    }
}

print(result)