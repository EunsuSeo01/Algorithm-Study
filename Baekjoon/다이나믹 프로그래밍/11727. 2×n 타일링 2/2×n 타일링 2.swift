import Foundation

var dp = Array(repeating: 0, count: 1001)
let N = Int(readLine()!)!

dp[1] = 1
if N != 1 {
    for i in 2...N {
        if i % 2 == 0 {
            dp[i] = (dp[i - 1] * 2 + 1) % 10007
        } else {
            dp[i] = (dp[i - 1] * 2 - 1) % 10007
        }
    }
}

print(dp[N])