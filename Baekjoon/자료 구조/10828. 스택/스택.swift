import Foundation

var stack: [Int] = []

let N = Int(readLine()!)!

for _ in 0..<N {
    let input = readLine()!.split(separator: " ")
    switch input[0] {
    case "push":
        stack.append(Int(input[1])!)
    case "pop":
        if let res = stack.popLast() {
            print(res)
        } else {
            print(-1)
        }
    case "empty":
        print(stack.isEmpty ? 1 : 0)
    case "size":
        print(stack.count)
    case "top":
        if let top = stack.last {
            print(top)
        } else {
            print(-1)
        }
    default:
        break
    }
}