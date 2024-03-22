import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0]
var count = 0

var numbers = readLine()!.split(separator: " ").map { Int($0)! }
var queue: [Int] = []

for i in 1...N {
    queue.append(i)
}

var front = 0
var rear = queue.count - 1

while true {
    if numbers.isEmpty {
        break
    }
    if let idx = queue.firstIndex(of: numbers[0]) {
        if queue[0] != numbers[0] {
            if idx <= abs(idx - (queue.count - 1)) {
                for _ in 0..<idx {
                    queue.append(queue.first!)
                    queue.removeFirst()
                    count += 1
                }
            } else {
                for _ in 0...abs(idx - (queue.count - 1)) {
                    queue = Array(arrayLiteral: queue.last!) + queue
                    queue.removeLast()
                    count += 1
                }
            }
        } else {
            queue.removeFirst()
            numbers.removeFirst()
        }
    }
}

print(count)