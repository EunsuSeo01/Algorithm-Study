import Foundation

let T = Int(readLine()!)!

for _ in 0..<T {
    let arr = readLine()!
    var left = ""
    var right = ""
    
    for i in arr {
        switch i {
        case "<":
            if !left.isEmpty {
                guard let last = left.popLast() else { break }
                right.append(last)
            }
        case ">":
            if !right.isEmpty {
                guard let last = right.popLast() else { break }
                left.append(last)
            }
        case "-":
            if !left.isEmpty {
                left.removeLast()
            }
        default:
            left.append(i)
        }
    }
    
    if !right.isEmpty {
        for j in right.reversed() {
            left.append(j)
        }
    }
    
    print(left)
}