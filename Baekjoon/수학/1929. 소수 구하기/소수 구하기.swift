import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
var M = input[0]
var N = input[1]
var arr: [Bool] = Array(repeating: true, count: N+1)
arr[0] = false
if N >= 1 { arr[1] = false }

if M == 1 && N == 1 {
    print(0)
    exit(0)
}

if N > 2 {
    for i in 2..<Int(sqrt(Double(N))+1) {
        if arr[i] {
            for j in stride(from: i*i, to: N+1, by: i) {
                arr[j] = false
            }
        }
    }
}

for i in M...N {
    if arr[i] {
        print(i)
    }
}
