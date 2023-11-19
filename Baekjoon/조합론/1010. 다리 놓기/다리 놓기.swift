import Foundation

let T = Int(readLine()!)!
var dp: [[Int]] = Array(repeating: Array(repeating: 0, count: 31), count: 31)

// m개 중에 1개 고르는 거
for m in 1...30 {
    dp[1][m] = m;
}
// m개 중에 n개 고르는 거
for n in 2...30 {
    for m in 2...30 {
        dp[n][m] = dp[n-1][m-1] + dp[n][m-1]
    }
}

for _ in 0..<T {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    print(dp[input[0]][input[1]])
}