import Foundation

var N = Int(readLine()!)!
var input = readLine()!.split(separator: " ").map { Int($0)! }
var ans = 0

for i in input {
    var cnt = 0
    for j in 1...i {
        if i % j == 0 {
            cnt += 1
        }
    }
    if cnt == 2 {
        ans += 1
    }
}

print(ans)