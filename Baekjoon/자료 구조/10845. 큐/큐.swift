import Foundation

let N = Int(readLine()!)!
var queue: [Int] = []

for _ in 0..<N {
    let command = readLine()!.split(separator: " ")
    if command.count == 1 {
        switch command[0] {
        case "pop":
            print(queue.first ?? -1)
            if !queue.isEmpty {
                queue.removeFirst()
            }
        case "size":
            print(queue.count)
        case "empty":
            print(queue.isEmpty ? 1 : 0)
        case "front":
            print(queue.first ?? -1)
        case "back":
            print(queue.last ?? -1)
        default:
            break
        }
    } else {
        queue.append(Int(command[1])!)
    }
}