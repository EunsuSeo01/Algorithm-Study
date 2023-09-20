import Foundation

let N = Int(readLine()!)!

for _ in 0..<N {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    var a = input[0]
    var b = input[1]
    var answer = a * b
    
    if a < b {
        let tmp = a
        a = b
        b = tmp
    }
    
    var r = 1
    while b != 0 {
        r = a % b
        a = b
        b = r
    }
    
    print(answer / a)
}