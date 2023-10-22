import Foundation

let N = Int(readLine()!)!
var ropes: [Int] = []
var answers: [Int] = []

for _ in 0..<N {
    ropes.append(Int(readLine()!)!)
}
ropes.sort(by: >)

for i in 1...ropes.count {
    answers.append(ropes[i-1] * i)
}

print(answers.max()!)