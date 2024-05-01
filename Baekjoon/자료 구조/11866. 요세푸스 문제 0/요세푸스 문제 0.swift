import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
var queue: [Int] = []
var order = 1
var answer: [String] = []

for i in 1...input[0] {
    queue.append(i)
}

while !queue.isEmpty {
    guard let first = queue.first else { break }
    if order == input[1] {
        answer.append(String(first))
        queue.removeFirst()
        order = 1
    } else {
        queue.removeFirst()
        queue.append(first)
        order += 1
    }
}

print("<" + answer.joined(separator: ", ") + ">")