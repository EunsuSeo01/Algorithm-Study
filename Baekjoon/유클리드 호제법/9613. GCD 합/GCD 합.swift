import Foundation

let t = Int(readLine()!)!
var result = 0
var isEnded = false

func gcd(_ n1: Int, _ n2: Int) -> Int {
    if n2 == 0 {
        return n1
    }
    return gcd(n2, n1 % n2)
}

for _ in 0..<t {
    result = 0
    let line = readLine()!.split(separator: " ").map { Int($0)! }
    let num = line[0]
    for i in 1..<num {
        for j in i+1...num {
            result += gcd(line[i], line[j])
        }
    }
    print(result)
}