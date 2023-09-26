import Foundation

let N = Int(readLine()!)!
var input = readLine()!.split(separator: " ").map { Int($0)! }
var arr = input.enumerated().map{ ($0+1, $1) }
var answer = ""
var step = 0

step = arr[0].1
answer = "\(arr[0].0) "
arr.remove(at: 0)

while !arr.isEmpty {
    if step < 0 {
        step = abs(step)
        for _ in 0..<step {
            arr.insert(arr.popLast()!, at: 0)
        }
    } else {
        step -= 1
        for _ in 0..<step {
            arr.append(arr[0])
            arr.remove(at: 0)
        }
        
    }
    
    step = arr[0].1
    answer += "\(arr[0].0) "
    arr.remove(at: 0)
}

print(answer)